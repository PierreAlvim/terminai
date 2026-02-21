# Terminai 🚀

A lightning-fast terminal AI assistant designed for developers who live in the shell. Terminai provides concise answers and **injects commands directly into your terminal buffer**.

## ✨ Features

- **Command Injection**: Suggested commands are placed directly into your input line. Review, edit, and press Enter.
- **Interactive Mode**: Run `q?` without arguments to enter an interactive prompt—perfect for complex queries with special characters.
- **Unquoted Prompts**: Natural language support. Just type `q? how to do x`.
- **Case Insensitive**: Use `q?` or `Q?` as you prefer.
- **Beautiful UI**: Powered by `rich` for markdown rendering and clean output.
- **Isolated Installation**: Uses a dedicated virtual environment to avoid system conflicts.

---

## 🛠️ Setup Tutorial

Follow these steps to get Terminai up and running on your system.

### 1. Installation
Run the automated installation script. This will create a private virtual environment and set up the Fish shell functions.
```bash
chmod +x install.sh
./install.sh
```

### 2. Get a Gemini API Key
If you don't have one, visit the [Google AI Studio](https://aistudio.google.com/app/apikey) to generate your free API key.

### 3. Configure Terminai
Run the setup command. It will ask for your key, validate it with a test call, and save it securely.
```fish
q? --setup
```
> [!TIP]
> Your input will be masked with `*` for security.

---

## 🚀 Usage

### Simple Queries (Unquoted)
Best for quick help without special shell characters.
```fish
q? list files larger than 100mb
```

### Interactive Mode
Best for complex queries or when you want to use characters like `|`, `>`, `&`, or `*` without quoting.
```fish
q?
# Opens a prompt:
Question? find . -name "*.log" | xargs grep "error"
```

### Quoted Queries
Use quotes if you want to include shell characters in a single-line command.
```fish
q? "how to use awk to print the second column of a csv"
```

---

## 🛠️ Technology Stack
- **AI**: Google Gemini (via `google-generativeai`)
- **CLI**: Python + `click` + `rich`
- **Shell**: Native Fish Shell integration
- **Security**: `pwinput` for masked API key entry
