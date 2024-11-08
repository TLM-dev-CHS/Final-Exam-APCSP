from py.Global import *

import customtkinter as ctk

from py.Directories import *
from py.InternetCheck import *
from py.Updater import Updater


class Launcher:
    def __init__(self):
        self.launch()

    def launch(self):
        INetCheck()
        PathChecks()
        Updater()

Launcher()