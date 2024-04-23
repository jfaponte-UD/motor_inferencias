
from src.Entity.Conditions import Conditions
from src.Entity.Hypothesis import Hypothesis


def add_condition():
    attribute = str(input("Ingresa un atributo: "))
    value = str(input("Ingresa un valor: "))
    logic_operator = str(input("Ingresa un operador logico: "))

    condition = Conditions(attribute, value, logic_operator)

    print("Regla creada: ", "VALOR: ", condition.value, "ATRIBUTO: ", condition.attribute, "OPERADOR: ",
          condition.logic_operator)

    while True:
        print("DESEAS AGREGAR OTRA REGLA")
        print("1. SI")
        print("2. NO")

        option_con = input("Ingrese una opcion: ")

        if int(option_con) == 1:
            add_condition()
        if int(option_con) == 2:
            print("Saliendo... ")
            break


def add_hypothesis():
    print("\n\n--- CREA LA HIPOTESIS INICIAL ---")
    attribute = str(input("Ingresa un atributo: "))
    value = str(input("Ingresa un valor: "))

    hypothesis = Hypothesis(attribute, value)

    print("Hipotesis creada: ", "VALOR: ", hypothesis.value, "ATRIBUTO: ", hypothesis.attribute)

    while True:
        print("\n --- MENU DE OPCIONES DE HIPOTESIS ", hypothesis.attribute, " ---")
        print("1. Agregar condicion")
        print("2. Salir")

        option_hyp = input("Ingrese una opcion: ")

        if int(option_hyp) == 1:
            add_condition()
        if int(option_hyp) == 2:
            print("Saliendo... ")
            break


def backward_chaining():
    print("backward")


if __name__ == '__main__':

    while True:
        print("MENU DE OPCIONES")
        print("1. Crear Hipotesis")
        print("2. Encadenamiento hacia atras")
        print("3. Salir")

        option = input("Ingresa una opcion: ")

        if int(option) == 1:
            add_hypothesis()
        if int(option) == 2:
            backward_chaining()
        if int(option) == 3:
            print("Saliendo... ")
            break
