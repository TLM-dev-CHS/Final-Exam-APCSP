# --- Imports --- #
import customtkinter as ctk
from colorama import *
import logging
import os

APP_NAME = "Demo"

# --- Global Constants --- #

# Path:
CURRENT_DIR = os.getcwd()

# --- Global Procedures --- #
def inputSyntax(message, options):
    while True:
        OPTIONS_LIST = [f"{repr(option.lower())}" for option in options]
        choice = input(f"{message}\n\nOptions are {OPTIONS_LIST}.")

        if choice.lower() in OPTIONS_LIST:
            return True
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
