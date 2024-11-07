import subprocess
import logging
from colorama import Fore, Style

ONLINE_STATUS = None

from .Global import *

class iNetCheck():
    def __init__(self):
        self.launch()

    def launch(self):
        self.ONLINE_STATUS = self.pingCheck()
        if self.ONLINE_STATUS:
            logging.info(f"{Fore.GREEN}Internet connection detected!{Style.RESET_ALL}")
            return self.ONLINE_STATUS
        else:
            logging.error(f"{Fore.RED}No internet connection!{Style.RESET_ALL}")
            return not self.ONLINE_STATUS

    def pingCheck(self):
        pingHost = "8.8.8.8"

        result = subprocess.run(
            ['ping', '-c', '1', pingHost],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            return True
        else:
            logging.error(f"{Fore.RED}'ping' command not found.")

    def isOnline(self):
        return self.ONLINE_STATUS