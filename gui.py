from tkinter import *

class Gui():
    def __init__(self, graph):
        self.main_window = Tk()
        self.main_window.geometry("400x400")
        self.graph = graph

    def createMainWindow(self):
        text_area = Text(self.main_window, width=20, height=10)
        text_area.pack(side="top")
        buttonsframe = Frame(self.main_window)
        buttonsframe.pack(side="top", padx=20, pady=20)
        from_adj_matrix = lambda: self.graph.createFromAdjMatrix(
            text_area.get("1.0",END))
        from_inc_matrix = lambda: self.graph.createFromIncMatrix(
            text_area.get("1.0",END))
        from_adj_list = lambda: self.graph.createFromAdjList(
            text_area.get("1.0",END))
        adjacent_button = Button(buttonsframe,
            text="Macierz sąsiedztwa", command=from_adj_matrix)
        incidence_button = Button(buttonsframe,
            text="Macierz incydencji", command=from_inc_matrix)
        adjlist_button = Button(buttonsframe,
            text="Lista sąsiedztwa", command=from_adj_list)
        adjacent_button.pack(pady=10)
        incidence_button.pack(pady=10)
        adjlist_button.pack(pady=10)
        self.main_window.mainloop()
