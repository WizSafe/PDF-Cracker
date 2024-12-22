import pikepdf
from tqdm import tqdm
from time import sleep
from colorama import Fore, Style, init
from rich.console import Console
from rich.progress import track

# Initialize colorama
init()
console = Console()

# Banner with color
console.print("[bold magenta]########################################[/bold magenta]")
console.print("[bold cyan]#          PDF Password Cracker        #[/bold cyan]")
console.print("[bold magenta]########################################\n[/bold magenta]")

# Input from the user
pdf_path = input(Fore.YELLOW + "[?] Enter the PDF file path: " + Style.RESET_ALL)
wordlist_path = input(Fore.YELLOW + "[?] Enter the wordlist file path: " + Style.RESET_ALL)

# Brute-force function
try:
    passwords = [line.strip() for line in open(wordlist_path, "r", encoding="latin-1")]
    console.print("\n[bold green][*] Starting brute-force attack...[/bold green]\n")

    for password in track(passwords, description="[cyan]Trying passwords...[/cyan]"):
        try:
            with pikepdf.open(pdf_path, password=password):
                console.print(f"\n[bold green][+] Password found: {password}[/bold green]")
                break
        except pikepdf._core.PasswordError:
            console.print(f"[red][-] Trying password:[/red] {password}", end="\r")
            sleep(0.05)
    else:
        console.print("\n[bold red][-] Password not found. Try a bigger wordlist.[/bold red]")

except FileNotFoundError:
    console.print("\n[bold red][!] File not found. Check your paths again.[/bold red]")
