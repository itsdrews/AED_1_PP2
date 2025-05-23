#clase de referencia para nós em todas as árvores
class Node:
    def __init__(self, value):
        self.value = value
        self.name = None
        self.left = None
        self.right = None
        self.height = 1

    def set_name(self, name):
        self.name = name

    def to_string(self):
        return str(f"Nó {self.value}, nome associado: {self.name}")