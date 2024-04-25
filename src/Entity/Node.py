# NODO
# Condiciones:
#   A = V
# Hipotesis:
#   W Entonces V

class Node:
    def __init__(self, attribute: str, value: str, conditions: list = []):
        self.attribute: str = attribute
        self.value: str = value
        self.conditions: list = conditions
        self.edges: list = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def addCondition(self, condition):
        self.conditions.append(condition)
