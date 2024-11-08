# --- Standard Library Imports --- #
import subprocess

# --- Local Imports --- #
from .Global import *

# --- Internet Connection Checker Class --- #
class INetCheck:
    """
    Checks and stores the internet connection status.
    """

    def __init__(self):
        self.pingHost = None
        self.ONLINE_STATUS = None

        self.launch()

    def launch(self):
        self.ONLINE_STATUS = self.pingCheck()

        logging.info("Checking internet connection...")

        if self.ONLINE_STATUS:
            logging.info(f"{Fore.GREEN}Internet connection detected!{Style.RESET_ALL}")
        else:
            logging.error(f"{Fore.RED}No internet connection!{Style.RESET_ALL}")


    def pingCheck(self):
        self.pingHost = "8.8.8.8"

        result = subprocess.run(
            ['ping', '-c', '1', self.pingHost],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            return True
        else:
            return False

    def isOnline(self):
        return self.ONLINE_STATUS

# --- Main Execution --- #
if __name__ == "__main__":
    INetCheck()
