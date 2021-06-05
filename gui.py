from tkinter import *

class Gui():
    def __init__(self, graph):
        self.main_window = Tk()
        self.main_window.geometry("400x400")
        self.graph = graph
        self.buttonsframe = Frame(self.main_window)
        self.text_area = Text(self.main_window, width=20, height=10)

    def createMainWindow(self):
        self.text_area.pack(side="top")
        self.buttonsframe.pack(side="top", padx=20, pady=20)
        self.__createButton("Macierz sąsiedztwa", lambda:
            self.graph.createFromAdjMatrix(self.text_area.get("1.0",END)))
        self.__createButton("Macierz incydencji", lambda:
            self.graph.createFromIncMatrix(self.text_area.get("1.0",END)))
        self.__createButton("Lista sąsiedztwa", lambda:
            self.graph.createFromAdjList(self.text_area.get("1.0",END)))
        self.main_window.mainloop()

    def __createButton(self, text, onClick):
        button = Button(self.buttonsframe, text=text, command=onClick)
        button.pack(pady=10)
