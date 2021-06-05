from graph import Graph
import unittest

class Test_graph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def testCreateFromAdjMatrix(self):
        input = "0 1 1 0 0\n1 0 1 1 0\n1 1 0 1 0\n0 1 1 0 1\n0 0 0 1 0\n"
        self.graph.createFromAdjMatrix(input)
        self.assertEqual(self.graph.G.number_of_nodes(), 5)
        self.assertEqual(self.graph.G.number_of_edges(), 6)

    def testCreateFromIncMatrix(self):
        input = ("1 1 0 0 0 0\n1 0 1 1 0 0\n0 1 1 0 1 0\n0 0 0 1 1 1\n"
            "0 0 0 0 0 1\n")
        self.graph.createFromIncMatrix(input)
        self.assertEqual(self.graph.G.number_of_nodes(), 5)
        self.assertEqual(self.graph.G.number_of_edges(), 6)

    def testCreateFromAdjList(self):
        input = "1 2 3\n2 1 3 4\n3 1 2 4\n4 2 3 5\n5 4\n"
        self.graph.createFromAdjList(input)
        self.assertEqual(self.graph.G.number_of_nodes(), 5)
        self.assertEqual(self.graph.G.number_of_edges(), 6)
