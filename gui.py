from tkinter import *

class Gui():
    def __init__(self):
        self.main_window = Tk()
        self.main_window.geometry("400x400")

    def createMainWindow(self):
        text_area = Text(self.main_window, width=20, height=10)
        text_area.pack(side="top")
        self.main_window.mainloop()
