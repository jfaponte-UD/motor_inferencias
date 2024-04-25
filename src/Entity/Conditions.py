class Conditions:
    def __init__(self, attribute: str, value: str, logic_operator: str, math_operator: str):
        self.attribute = attribute
        self.value = value
        self.logic_operator = logic_operator
        self.math_operator = math_operator
