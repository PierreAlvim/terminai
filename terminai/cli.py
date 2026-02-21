import sys
import click
from rich.console import Console
from rich.markdown import Markdown
from .ai import get_ai_response, validate_api_key
from .config import set_api_key

console = Console(stderr=True)

@click.command()
@click.argument('prompt', nargs=-1)
@click.option('--setup', is_flag=True, help='Configure API key')
def main(prompt, setup):
    if setup:
        console.print("[bold blue]Terminai Setup[/bold blue]")
        console.print("Please enter your Gemini API key. [italic](You will see * as you type)[/italic]")
        import pwinput
        api_key = pwinput.pwinput(prompt="API Key: ", mask="*")
        
        if not api_key:
            console.print("[yellow]Input aborted.[/yellow]")
            return
        
        with console.status("[bold green]Validating API key..."):
            is_valid, message = validate_api_key(api_key)
            
        if is_valid:
            set_api_key(api_key)
            console.print("[bold green]✓ API key validated and saved successfully![/bold green]")
        else:
            console.print(f"[bold red]✗ Validation failed:[/bold red] {message}")
            console.print("[yellow]Please check your key and try again.[/yellow]")
        return



    if not prompt:
        # console.print("[bold cyan]Q?[/bold cyan] ")
        prompt_text = click.prompt("Question", prompt_suffix="? ")
        if not prompt_text:
            return
        full_prompt = prompt_text
    else:
        full_prompt = " ".join(prompt)

    
    with console.status("[bold green]Thinking..."):
        explanation, command = get_ai_response(full_prompt)

    if explanation.startswith("Error"):
        console.print(f"[red]{explanation}[/red]")
        return

    # Print explanation to stderr
    console.print(Markdown(explanation))
    
    # Print command to stdout for the shell function to capture
    if command:
        print(command, end="", flush=True)


if __name__ == "__main__":
    main()
