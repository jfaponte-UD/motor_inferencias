from src.Entity.Node import Node

allHypothesis = {}

def validateRule(condition):
    facts = [
        { "A": "true" },
        { "B": "true" },
        { "C": "true" },
    ]

    for fact in facts:
        for attribute, value in fact.items():
            if isinstance(condition, Node):
                if condition.attribute == attribute and condition.value == value: return True
            else:
                if condition.get("attribute") == attribute and condition.get("value") == value: return True
                
    return False

def backwardChaining(hypothesis):
    band = False
    for condition in hypothesis.conditions:
        if isinstance(condition, Node):
            print("Hipotesis: " + condition.attribute + " => " + condition.value)
            backwardChaining(condition)
        else:
            print("Condicion: " + condition.get("attribute") + " => " + condition.get("value"))
            band = validateRule(condition)
            print("Condicion en base de hechos: " + str(band) + "\n")

def loadExample():
    allHypothesis[1] = Node("D", "true", [{ "attribute": "A", "value": "true"}])
    allHypothesis[2] = Node("F", "true", [allHypothesis[1], { "attribute": "B", "value": "true"}])
    allHypothesis[3] = Node("H", "true", [allHypothesis[2], { "attribute": "G", "value": "true"}])
    allHypothesis[4] = Node("I", "true", [{ "attribute": "C", "value": "true"}])
    allHypothesis[5] = Node("W", "true", [allHypothesis[3], allHypothesis[4]])
    allHypothesis[6] = Node("W", "true", [allHypothesis[3], { "attribute": "J", "value": "true"}])
    allHypothesis[7] = Node("G", "true", [{ "attribute": "B", "value": "true"}])

def menuBackwardChaining():
    print("\n\n--- ENCADENAMIENTO HACIA ATRAS ---")
    for index, hypothesis in allHypothesis.items():
        print(str(index) + ". " + hypothesis.attribute + " => " + hypothesis.value)

    num = int(input("Escoja la hipotesis: "))

    backwardChaining(allHypothesis[num])
    

def menuAddCondition(): 
    attribute = str(input("Ingresa un atributo: "))
    value = str(input("Ingresa un valor: "))

    #print("Regla creada:", "ATRIBUTO: ", attribute, "VALOR: ", value)
    
    return { "attribute": attribute, "value": value }


def menuAddHypothesis():
    print("\n\n--- CREAR HIPOTESIS ---")
    attribute = str(input("Ingresa un atributo: "))
    value = str(input("Ingresa un valor: "))


    hypothesis = Node(attribute, value)
    print("Hipotesis creada: ", "ATRIBUTO: ", hypothesis.attribute, "VALUE: ", hypothesis.value)

    allHypothesis[len(allHypothesis) + 1] = hypothesis
    print(allHypothesis)

    while True:
        print("\n --- MENU DE OPCIONES DE HIPOTESIS ", hypothesis.attribute, " ---")
        print("1. Agregar condicion")
        #print("2. TODO:Agregar hipotesis como condicion")
        print("3. Salir")

        option_hyp = input("Ingrese una opcion: ")

        if int(option_hyp) == 1:
            hypothesis.addCondition(menuAddCondition())
        if int(option_hyp) == 3:
            print("\nSaliendo... ")
            break


if __name__ == '__main__':
    # Si el nodo tiene condiciones es una hipotesis, de lo contrario es solo una condición
    # conditionsPerro = [ { "attribute": "num_patas", "value": "4" }, { "attribute": "pelaje", "value": "corto" } ]
    
    # hypothesisPerro = Node(
    #     "animal", 
    #     "perro", 
    #     conditionsPerro
    # )

    # conditionsPitbull = [
    #     { "attribute": "tamaño", "value": "pequeño" }, 
    #     hypothesisPerro
    # ]

    # hypothesisPitbull = Node("raza", "pitbull", conditionsPitbull)

    while True:
        print("\n\nMENU DE OPCIONES")
        print("1. Crear Hipotesis")
        print("2. Encadenamiento hacia atras")
        print("3. Cargar ejemplo")
        print("9. Salir")

        option = input("Ingresa una opcion: ")

        if int(option) == 1:
            menuAddHypothesis()
        if int(option) == 2:
            menuBackwardChaining()
        if int(option) == 3:
            loadExample()
        if int(option) == 9:
            print("\nSaliendo... ")
            break

    # Se pasa la hipotesis a validar
    # backwardChaining(hypothesisPitbull)

