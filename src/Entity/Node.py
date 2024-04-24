from __future__ import annotations


class Node:
    def __init__(self, attribute: str, value: str):
        self.attribute = attribute
        self.value = value
        self.edges: list = []

    def add_edge(self, edge):
        self.edges.append(edge)
