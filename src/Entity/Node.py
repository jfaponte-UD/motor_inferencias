# NODO
# Condiciones:
#   A = V
# Hipotesis:
#   W Entonces V

from src.Entity.Hypothesis import Hypothesis
from src.Entity.Conditions import Conditions

class Node:
    def __init__(self, hypothesis: Hypothesis, conditions: list[Conditions] = None):
        self.hypothesis: Hypothesis = hypothesis
        self.conditions: list = conditions
        self.edges: list = []

    def add_edge(self, edge):
        self.edges.append(edge)
