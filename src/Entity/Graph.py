from src.Entity.Edge import Edge
from src.Entity.Node import Node


class Graph:
    def __init__(self, node1: Node, node2: Node):
        self.nodes: list[Node] = []
        self.add_edge(node1, node2)

    def add_edge(self, node1: Node, node2: Node):
        if node1 and node2:
            edge = Edge(node1, node2)
            node1.add_edge(edge)
            node2.add_edge(edge)
