import sys
from gui import run_gui
from cli import run_cli

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        run_cli()
    else:
        run_gui()  # Default to GUI mode