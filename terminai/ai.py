import warnings
# Suppress the deprecation warning from google-generativeai
warnings.simplefilter("ignore", category=FutureWarning)


import google.generativeai as genai
import re
from .config import get_api_key

SYSTEM_PROMPT = """
You are Terminai, a terminal-based AI assistant.
Your goal is to provide extremely concise answers to user queries, primarily focused on shell commands (Linux/Fish).
If the user asks for a command, provide a brief explanation (1-2 sentences) followed by the command itself.
Formatting rules:
1. Always wrap the primary shell command in triple backticks with 'bash' or 'fish' language.
2. Example: 
   To list files by size:
   ```bash
   ls -S
   ```
3. Keep explanations minimal.
4. If there are multiple ways, pick the most common one.
"""

def get_available_model(api_key):
    try:
        genai.configure(api_key=api_key)
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Prefer gemini-1.5-flash
        preferred = ["models/gemini-1.5-flash", "models/gemini-1.5-flash-latest", "models/gemini-pro"]
        for p in preferred:
            if p in models:
                return p
        
        # Return first available if preferred not found
        return models[0] if models else "models/gemini-1.5-flash"
    except Exception:
        return "models/gemini-1.5-flash"

def validate_api_key(api_key):
    try:
        genai.configure(api_key=api_key)
        model_name = get_available_model(api_key)
        model = genai.GenerativeModel(model_name)
        # Simple test call
        model.generate_content("ping")
        return True, "API Key is valid."
    except Exception as e:
        return False, str(e)

def get_ai_response(prompt):
    api_key = get_api_key()
    if not api_key:
        return "Error: API key not found. Please run 'Q? --setup' to configure it.", None

    try:
        genai.configure(api_key=api_key)
        model_name = get_available_model(api_key)
        model = genai.GenerativeModel(model_name, system_instruction=SYSTEM_PROMPT)
        
        response = model.generate_content(prompt)

        text = response.text
        
        # Extract the first code block as the suggested command
        command = None
        match = re.search(r'```(?:bash|fish|sh)?\n(.*?)\n```', text, re.DOTALL)
        if match:
            command = match.group(1).strip()
        
        return text, command
    except Exception as e:
        return f"Error: {str(e)}", None
