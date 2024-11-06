# --- Imports --- #
### * Standard Python Imports:
import logging
import os

### * Third-Party Imports:
import customtkinter as ctk
from colorama import *
import requests
from requests import options

### * Local Imports:
from Global import *

ONLINE_VERSION_URL = f"{RAW_REPO_URL}/config/version.txt"

class Updater(ctk.CTk):
    def __init__(self):
        self.LOCAL_VERSION = None
        self.ONLINE_VERSION = None

        logging.info("Checking for updates...")

        self.checkVersions()
        self.updateHandler()

    def checkVersions(self):
        logging.info("Checking for new versions...")

        self.LOCAL_VERSION = APP_VERSION
        self.ONLINE_VERSION = requests.get(ONLINE_VERSION_URL).text

        logging.info(f"The local version is {repr(self.LOCAL_VERSION)}.")
        logging.info(f"The online version is {repr(self.ONLINE_VERSION)}.")

    def updateHandler(self):
        LV = int(self.LOCAL_VERSION.replace(".", ""))
        OV = int(self.ONLINE_VERSION.replace(".", ""))

        if LV == OV:
            logging.info(f"{Fore.GREEN}{APP_NAME} is already up to date, have a good day!")
        elif LV < OV:
            logging.info(f"{Fore.YELLOW}An update is available...")
            CHOICE = inputSyntax("Would you like to update?", ["Yes", "No"])
            if CHOICE == "yes".casefold():
                self.updater()
            else:
                logging.info("Update cancelled, have a good day!")

    def updater(self):
        logging.info(f"{Fore.YELLOW}Updating to version {self.ONLINE_VERSION}...")
        requests.get(f"{RAW_RELEASE_URL}/{self.ONLINE_VERSION}/{self.ONLINE_VERSION}")

Updater()