from py.Global import *

import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        self.button = None
        self.test()

    def test(self):
        super().__init__()
        self.title(APP_NAME)
        self.minsize(400, 200)
        self.resizable(False, False)

        self.button = ctk.CTkButton(self, text="test", command=self.Testing)
        self.button.pack()

        self.mainloop()

    def Testing(self):
        errorWindow("Testing")

App()