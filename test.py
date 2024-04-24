class Rule:
    def __init__(self, conclusion, conditions):
        self.conclusion = conclusion
        self.conditions = conditions


class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules

    def backward_chain(self, goal, facts, path=None):
        if path is None:
            path = []

        if goal in facts:
            print(f"Llegó a {goal} (hecho).")
            return True

        for rule in self.rules:
            if rule.conclusion == goal:
                print(f"Explorando regla: {rule.conclusion} -> {', '.join(rule.conditions)}")
                if all(self.backward_chain(condition, facts, path + [goal]) for condition in rule.conditions):
                    print(f"Llegó a {goal} (inferencia).")
                    # Retira los prints de camino y solo regresa el recorrido encontrado
                    return path + [goal]
        return []


# Ejemplo de uso
if __name__ == "__main__":
    # Definir reglas
    rules = [
        Rule("D", ["A"]),
        Rule("F", ["D", "B"]),
        Rule("H", ["F", "G"]),
        Rule("I", ["C"]),
        Rule("W", ["H", "I"]),
        Rule("W", ["H", "J"]),
        Rule("G", ["B"])
    ]

    # Hechos iniciales
    initial_facts = ["A", "B", "C"]

    # Motor de inferencia
    engine = InferenceEngine(rules)

    # # Inferencia
    goal = "W"
    if engine.backward_chain(goal, initial_facts):
        print(f"\nSe puede inferir que {goal} es verdadero.")
    else:
        print(f"\nNo se puede inferir que {goal} sea verdadero.")

