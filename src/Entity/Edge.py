from src.Entity.Node import Node


class Edge:
    def __init__(self, node_origin: Node, node_destination: Node):
        self.node_origin: Node = node_origin
        self.node_destination: Node = node_destination
