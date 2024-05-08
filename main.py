from src.Entity.Node import Node

allHypothesis = {}

def validateRule(condition):
    facts = [
        {"Leche": "false"},
        {"Pelo": "true"},
        {"Carne": "Come"},
        {"Dientes": "Puntiagudos"},
        {"Garras": "true"},
        {"Ojos": "Frente"},
        {"Color": "leonado_rayas"},
    ]

    for fact in facts:
        for attribute, value in fact.items():
            if isinstance(condition, Node):
                if condition.attribute == attribute and condition.value == value: return True
            else:
                if condition.get("attribute") == attribute and condition.get("value") == value: return True

    return False

conditions_results = []

def evaluateResults():
    global conditions_results
    if all(conditions_results):
        print("El objetivo es definitivamente Verdadero")
    else:
        print("El objetivo es definitivamente Falso")

def backwardChaining(hypothesis):
    global conditions_results

    for condition in hypothesis.conditions:
        if isinstance(condition, Node):
            print("Hipotesis: " + condition.attribute + " => " + condition.value)
            backwardChaining(condition)
        else:
            print("Condicion: " + condition.get("attribute") + " => " + condition.get("value"))
            result = validateRule(condition)
            conditions_results.append(result)
            print("Condicion en base de hechos: " + str(result) + "\n")

def loadExample():
    allHypothesis[1] = Node("Mamifero", "true", [{"attribute": "Pelo", "value": "true"}])
    allHypothesis[2] = Node("Mamifero", "true", [allHypothesis[1], {"attribute": "Leche", "value": "true"}])
    allHypothesis[3] = Node("Ave", "true", [{"attribute": "Plumas", "value": "true"}])
    allHypothesis[4] = Node("Ave", "true", [allHypothesis[3], {"attribute": "Huevos", "value": "true"}])
    allHypothesis[5] = Node("Carnivoro", "true", [{"attribute": "Carne", "value": "Come"}])
    allHypothesis[6] = Node("Carnivoro", "true", [allHypothesis[5], {"attribute": "Dientes", "value": "Puntiagudos"},
                                                  {"attribute": "Garras", "value": "true"},
                                                  {"attribute": "Ojos", "value": "Frente"}])
    allHypothesis[7] = Node("Ungulado", "true", [allHypothesis[2], {"attribute": "Pezuñas", "value": "true"}])
    allHypothesis[8] = Node("Ungulado", "true", [allHypothesis[2], {"attribute": "Rumia", "value": "true"}])
    allHypothesis[9] = Node("Leopardo", "true",
                            [allHypothesis[2], allHypothesis[6], {"attribute": "Color", "value": "leonado_manchas"}])
    allHypothesis[10] = Node("Tigre", "true",
                             [allHypothesis[2], allHypothesis[6], {"attribute": "Color", "value": "leonado_rayas"}])
    allHypothesis[11] = Node("Jirafa", "true", [allHypothesis[8], {"attribute": "Cuello", "value": "largo"},
                                                {"attribute": "Piernas", "value": "largo"},
                                                {"attribute": "machas", "value": "true"}])
    allHypothesis[12] = Node("Cebra", "true", [allHypothesis[8], {"attribute": "Rayas", "value": "Negras"}])
    allHypothesis[13] = Node("Avestruz", "true", [allHypothesis[4], {"attribute": "Vuela", "value": "false"},
                                                  {"attribute": "Cuello", "value": "largo"},
                                                  {"attribute": "Piernas", "value": "largo"},
                                                  {"attribute": "Color", "value": "blanco_negro"}])
    allHypothesis[14] = Node("Pinguino", "true", [allHypothesis[4], {"attribute": "Vuela", "value": "false"},
                                                  {"attribute": "Nada", "value": "true"},
                                                  {"attribute": "Cuello", "value": "corto"},
                                                  {"attribute": "Piernas", "value": "corto"},
                                                  {"attribute": "Color", "value": "blanco_negro"}])
    allHypothesis[15] = Node("Albatros", "true", [allHypothesis[4], {"attribute": "Vuela", "value": "true"}])
    allHypothesis[16] = Node("Misma_especie", "true", [{"attribute": "Padre", "value": "true"}])



def menuBackwardChaining():
    print("\n\n--- ENCADENAMIENTO HACIA ATRAS ---")
    for index, hypothesis in allHypothesis.items():
        print(str(index) + ". " + hypothesis.attribute + " => " + hypothesis.value)

    num = int(input("Escoja la hipotesis: "))

    backwardChaining(allHypothesis[num])


def menuAddCondition():
    attribute = str(input("Ingresa un atributo: "))
    value = str(input("Ingresa un valor: "))

    # print("Regla creada:", "ATRIBUTO: ", attribute, "VALOR: ", value)

    return {"attribute": attribute, "value": value}


if __name__ == '__main__':

    while True:
        print("\n\nMENU DE OPCIONES")
        print("1. Encadenamiento hacia atras")
        print("2. Cargar Base de conocimientos")
        print("9. Salir")

        option = input("Ingresa una opcion: ")

        if int(option) == 1:
            menuBackwardChaining()
            evaluateResults()
        if int(option) == 2:
            loadExample()
        if int(option) == 9:
            print("\nSaliendo... ")
            break

    # Se pasa la hipotesis a validar
    # backwardChaining(hypothesisPitbull)
