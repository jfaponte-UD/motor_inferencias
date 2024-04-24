class Rule:
    def __init__(self, conclusion, conditions):
        self.conclusion = conclusion
        self.conditions = conditions


class InferenceEngine:

    def __init__(self, rules):
        self.rules = rules

    def backward_chain(self, goal, facts):
        # Base case: Si la meta ya está en los hechos, simplemente devolvemos la meta
        if goal in facts:
            return [goal]

        # Iteramos sobre todas las reglas
        for rule in self.rules:
            # Si la conclusión de la regla es igual a la meta
            if rule.conclusion == goal:
                # Verificamos si todas las condiciones de la regla se pueden inferir recursivamente
                for condition in rule.conditions:
                    # Intentamos inferir la condición
                    condition_path = self.backward_chain(condition, facts)
                    # Si se pudo inferir la condición, devolvemos el camino encontrado hasta aquí
                    if condition_path:
                        return condition_path + [goal]
        # Si no pudimos inferir la meta, devolvemos None
        return None


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
    path = engine.backward_chain(goal, initial_facts)
    if path:
        print(f"\nSe puede inferir que {goal} es verdadero.")
        print("Camino encontrado:", path)
    else:
        print(f"\nNo se puede inferir que {goal} sea verdadero.")
