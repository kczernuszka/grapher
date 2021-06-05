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