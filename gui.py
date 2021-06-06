from tkinter import *

class Gui():
    def __init__(self, graph):
        self.main_window = Tk()
        self.main_window.geometry("700x400")
        self.graph = graph
        self.text_area = Text(self.main_window, width=20, height=10)

    def createMainWindow(self):
        self.text_area.grid(row=1, column=0, padx=15)

        self.__createLabel("Tworzenie grafu:", 0, 0)
        self.__createButton("Macierz sąsiedztwa", 2, 0, lambda:
            self.graph.createFromAdjMatrix(self.text_area.get("1.0",END)))
        self.__createButton("Macierz incydencji", 3, 0, lambda:
            self.graph.createFromIncMatrix(self.text_area.get("1.0",END)))
        self.__createButton("Lista sąsiedztwa", 4, 0, lambda:
            self.graph.createFromAdjList(self.text_area.get("1.0",END)))

        self.__createLabel("Kolorowanie grafu:", 0, 1)
        self.__createButton("Według etykiety", 2, 1, None)
        self.__createButton("Malejąco wg stopni wierzchołka", 3, 1, None)
        self.__createButton("Losowo", 4, 1, None)

        self.__createLabel("Przeszukiwanie grafu:", 0, 2)
        nodes_list = StringVar()
        self.__createButton("Przeszukiwanie w głąb", 2, 2, None)
        self.__createButton("Zaznacz krawędzie krytyczne", 3, 2, None)
        self.__createLabel("Wynik przeuszkiwania:", 4, 2)
        Label(self.main_window, textvariable=nodes_list)

        self.main_window.mainloop()

    def __createButton(self, text, row, column, onClick):
        (Button(self.main_window, text=text, command=onClick)
            .grid(row=row, column=column, padx=25, pady=10))

    def __createLabel(self, text, row, column):
        Label(self.main_window, text=text).grid(row=row, column=column)
