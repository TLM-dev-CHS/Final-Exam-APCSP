# --- Imports --- #
### * Standard Python Imports:
import logging
import os

### * Third-Party Imports:
import customtkinter as ctk
from colorama import *

# --- Global Constants --- #
### * App Constants:
APP_NAME = "File Size Sorter"
APP_VERSION = "1.0.0"
RAW_REPO_URL = "https://raw.githubusercontent.com/TLM-dev-CHS/Final-Exam-APCSP/refs/heads/main"
RAW_RELEASE_URL = "https://github.com/TLM-dev-CHS/Final-Exam-APCSP/releases/download/"

### * Path Constants:
CURRENT_DIR = os.getcwd()
paths = {
    "config": {
        "config.ini",
        "settings.ini"
    },
    "docs": {
        "DOCS.md",
        "HELP.md"
    },
    "tests": {
        "__init__.py",
        "Test.py"
    },
    "downloads": {
        "downloads.txt"
    }
}

### * Logging Setup:
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] - [%(levelname)s] - [%(filename)s] - %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

# --- Global Procedures --- #
def inputSyntax(message, options):
    while True:
        OPTIONS_LIST = [option.lower() for option in options]
        choice = input(f"{message}\n\nOptions are: {OPTIONS_LIST}.\n>>> ")

        if choice.lower() in OPTIONS_LIST:
            return choice.lower()
        else:
            logging.error(f"{Fore.RED}Invalid option, {choice} selected!{Style.RESET_ALL}")

def errorWindow(message):
    errWin = ctk.CTkToplevel()
    errWin.title("Error")
    errWin.minsize(400, 200)
    errWin.resizable(False, False)

    label = ctk.CTkLabel(errWin, text=message)
    label.pack(pady=10, padx=10)

    button = ctk.CTkButton(errWin, text="OK", command=errWin.destroy)
    button.pack(pady=10, padx=10)
