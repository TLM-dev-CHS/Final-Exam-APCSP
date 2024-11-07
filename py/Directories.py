from .Global import *

class PathChecks():
    def __init__(self):
        self.FOLDERS = []
        self.FILES = []

        self.FOLDERS_AND_FILES_EXIST = False

        self.launch()

    def launch(self):
        self.FOLDERS_AND_FILES_EXIST = self.makeDirs()

        if self.FOLDERS_AND_FILES_EXIST:
            logging.info(f"{Fore.GREEN}All folders and files exist!{Style.RESET_ALL}")
        else:
            logging.info("Creating file structure...")
            self.pathReader()
            logging.info(f"{Fore.YELLOW}Some folders or files were created.{Style.RESET_ALL}")

    def pathReader(self):
        logging.info("Reading paths...")

        for folder, files in paths.items():
            folderPath = os.path.join(CURRENT_DIR, folder)
            self.FOLDERS.append(folderPath)
            for file in files:
                filePath = os.path.join(CURRENT_DIR, folder, file)
                self.FILES.append(filePath)

        logging.info(f"{Fore.GREEN}All paths have been read successfully!{Style.RESET_ALL}")

    def makeDirs(self):
        allExist = True

        for folder in self.FOLDERS:
            if not os.path.exists(folder):
                os.makedirs(folder)
                logging.info(f"{Fore.YELLOW}Folder created at {repr(folder)}!{Style.RESET_ALL}")
                allExist = False

        if not allExist:
            logging.info(f"{Fore.GREEN}All folders have been created!{Style.RESET_ALL}")

        for file in self.FILES:
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    f.write("")
                logging.info(f"{Fore.YELLOW}File created at {repr(file)}!{Style.RESET_ALL}")
                allExist = False

        if not allExist:
            logging.info(f"{Fore.GREEN}All files have been created!{Style.RESET_ALL}")

        return allExist

    def fileFoldersExist(self):
        return self.FOLDERS_AND_FILES_EXIST