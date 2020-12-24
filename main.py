#===========================
# Imports
#===========================
import fire

import colorama
from colorama import Fore, Style, Back

import rich
from rich.console import Console

#===========================
# Main App
#===========================
class App:
    """Main Command-line Application."""
    colorama = colorama.init(autoreset=True)
    console = Console()

    # ------------------------------------------

def main():
    app = App()
    fire.Fire(app)

#===========================
# Start App
#===========================
if __name__ == '__main__':
    main()