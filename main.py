from src.Entity.Hypothesis import Hypothesis
from src.Entity.Conditions import Conditions
from src.Entity.Node import Node
from src.Entity.Edge import Edge
from src.Entity.Graph import Graph


def create_hypothesis():

    print("\n\n--- CREA LA HIPOTESIS INICIAL ---")
    attribute = str(input("Ingresa un atributo: "))
    value = str(input("Ingresa un valor: "))
    hypothesis = Hypothesis(attribute, value)

    print("Hipotesis creada: ", "VALOR:", hypothesis.value, "ATRIBUTO:", hypothesis.attribute)
    return hypothesis

def create_condition():

    attribute = str(input("Ingresa un atributo: "))
    value = str(input("Ingresa un valor: "))
    math_operator = str(input("Ingresa un operador matematico (=, !=, >, <): "))
    logic_operator = str(input("Ingresa un operador logico (AND, OR): "))


    condition = Conditions(attribute, value, logic_operator, math_operator)

    print("Condicion creada: ", condition.attribute, condition.math_operator, condition.value, condition.logic_operator)
    return condition

def create_node(hypothesis, conditions=None):
    return Node(hypothesis, conditions)

def create_graph():
    return Graph()

def show_conditions_hypothesis(hypothesis_attribute, graph):
    found_conditions = False
    for node in graph.nodes:
        if node.hypothesis.attribute == hypothesis_attribute:
            if node.conditions:
                found_conditions = True

                print(f"\n--- CONDICIONES PARA LA HIPOTESIS '{hypothesis_attribute}' ---")
                print("SI")
                for i, condition in enumerate(node.conditions):
                    print(f"{condition.attribute} {condition.math_operator} {condition.value} {condition.logic_operator}")

                print(f"ENTONCES {hypothesis_attribute} = {node.hypothesis.value}")
            else:
                print(f"La hipotesis '{hypothesis_attribute}' no tiene condiciones.")
            break

    if not found_conditions:
        print(f"No se encontró la hipotesis '{hypothesis_attribute}'.")

def build_graph():
    graph = create_graph()

    while True:
        print("\n--- CONSTRUYE EL GRAFO DE CONOCIMIENTO ---")
        print("1. Crear Hipotesis")
        print("2. Agregar Condicion a Hipotesis Existente")
        print("3. Mostrar Regla de una Hipotesis")
        print("4. Salir")

        option = input("Ingrese una opcion: ")

        if int(option) == 1:
            hypothesis = create_hypothesis()
            node = create_node(hypothesis)
            graph.nodes.append(node)
        elif int(option) == 2:
            if not graph.nodes:
                print("No hay hipotesis creadas para agregar condiciones.")
            else:
                print("\n--- HIPOTESIS EXISTENTES ---")
                for i, node in enumerate(graph.nodes):
                    print(f"{i+1}. ATRIBUTO: {node.hypothesis.attribute}, VALOR: {node.hypothesis.value}")
                choice = int(input("Elige la hipotesis para agregar condicion (ingresa el numero): "))
                if 1 <= choice <= len(graph.nodes):
                    selected_node = graph.nodes[choice - 1]
                    condition = create_condition()
                    if not selected_node.conditions:
                        selected_node.conditions = []
                    selected_node.conditions.append(condition)
                else:
                    print("Opcion invalida.")
        elif int(option) == 3:
            if not graph.nodes:
                print("No hay hipotesis creadas para mostrar condiciones.")
            else:
                hypothesis_attribute = str(input("Ingrese el atributo de la hipotesis para mostrar la regla: "))
                show_conditions_hypothesis(hypothesis_attribute, graph)
        elif int(option) == 4:
            print("Saliendo... ")
            break

    return graph

def main():
    graph = build_graph()

if __name__ == "__main__":
    main()
