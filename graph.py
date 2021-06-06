import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

class Graph():
    def __init__(self):
        self.G = nx.Graph()

    def createFromAdjMatrix(self, input):
        matrix = self.__getMatrixFromInput(input)
        self.G = nx.from_numpy_matrix(matrix)
        self.__drawGraph()

    def createFromIncMatrix(self, input):
        matrix = self.__getMatrixFromInput(input)
        am = self.__adjMatrixFromIncMatrix(matrix)
        self.G = nx.from_numpy_matrix(am)
        self.__drawGraph()

    def createFromAdjList(self, input):
        adj_list = input.splitlines()
        self.G = nx.parse_adjlist(adj_list, nodetype=int)
        self.__drawGraph()

    def colorGraph(self, strategy):
        d = nx.coloring.greedy_color(self.G,strategy=strategy)
        colors = [d[k] for k in sorted(d.keys())]
        plt.clf()
        nx.draw(self.G, with_labels=True, font_weight='bold', node_color=colors)

    def __getMatrixFromInput(self, input):
        input = input.replace("\n", ";")[:-1]
        return np.matrix(input)

    def __adjMatrixFromIncMatrix(self, matrix):
        am = (np.dot(matrix, matrix.T) > 0).astype(int)
        np.fill_diagonal(am, 0)
        return am

    def __drawGraph(self):
        plt.ion()
        plt.clf()
        nx.draw(self.G, with_labels=True, font_weight='bold')
        plt.show(block=False)
