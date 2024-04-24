from src.Entity.Edge import Edge
from src.Entity.Node import Node


class Graph:
    def __init__(self):
        self.nodes: list[Node] = []

    def add_node(self, attribute: str, value: str) -> Node:
        node = Node(attribute=attribute, value=value)
        self.nodes.append(node)
        return node

    @staticmethod
    def add_edge(node1: Node, node2: Node, rule: str):
        if node1 and node2:
            edge = Edge(node1, node2, rule)
            node1.add_edge(edge)
            node2.add_edge(edge)

    def backward_chaining(self, goal_node: Node) -> list[Node]:
        visited = set()
        stack = [(goal_node, None)]
        result = []

        while stack:
            current_node, parent_node = stack.pop()
            if current_node in visited:
                continue

            visited.add(current_node)

            if self.node_has_value(current_node, "True"):
                result.append(current_node)
                if parent_node:
                    print(f"De '{parent_node.attribute}' a '{current_node.attribute}'")

            for edge in current_node.edges:
                if edge.node_origin not in visited:
                    stack.append((edge.node_origin, current_node))
                    print(f"De '{current_node.attribute}' a '{edge.node_origin.attribute}'")

        return result

    @staticmethod
    def node_has_value(node: Node, value: str) -> bool:
        return node.value == value
