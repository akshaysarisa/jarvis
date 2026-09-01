
#jarvis v1 and v2 completed now v3 is here 
from rich.console import Console
from rich.prompt import Prompt
from llm import ask

console = Console()
console.print("[bold green]JARVISV3[/bold green]")
console.print("[bold yellow]Type 'exit' to quit[/bold yellow]")

while True:
    question = Prompt.ask("[bold blue]You[/bold blue]")
    if question.lower() == "exit":
        break
    try:
        answer = ask(question)
        console.print(f"[bold green]JARVISV3:[/bold green] {answer}")
    except Exception as e:
        console.print(
            f"[bold red]Error:[/bold red]{e}"
        )
