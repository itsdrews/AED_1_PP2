from BinarySearchTree import BinarySearchTree
from Node import Node
from BinaryTree import BinaryTree


class AVLTree(BinarySearchTree):
    def __init__(self):
        self.root = None
    def get_height(self,node:Node):
        return node.height if node else 0

    def get_balance(self,node:Node):
        return abs(self.get_height(node.left) - self.get_height(node.right)) if node else 0

    def _update_height(self, node: Node):
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
    def _rotate_right(self,y:Node):
        if y is None or y.left is None:
            return y
        # Rotaciona a direita o nó
        #print(f"Rodação á direita do {y.to_string()}")

        x = y.left
        aux = x.right 

        x.right = y
        y.left = aux

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self,x:Node):
        if x is None or x.right is None:
            return x
        # Rotaciona o nó a esquerda
        #print(f"Rodação á esquerda do {x.to_string()}")
        y = x.right
        aux = y.left 

        y.left = x
        x.right = aux

        self._update_height(x)
        self._update_height(y)

        return y


    def _balance(self,node:Node):
        self._update_height(node)
        factor = self.get_balance(node)

        # Rotacionando para esquerda
        if factor>1:
            if self.get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # Rotacionando para esquerda
        if factor<-1:
            if self.get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _insert_recursive(self,current:Node,key:str,name:str):
        
        if current is None:
            new_node = Node(key)
            new_node.set_name(name)
            return new_node
    
        if key < current.value:
            current.left = self._insert_recursive(current.left, key, name)
        elif key > current.value:
            current.right = self._insert_recursive(current.right, key, name)
        else:
            pass
        # Atualiza a altura do atual
        self._update_height(current)

        # Calcula o fator de balanceamento
        factor = self.get_balance(current)

        # Esquerda-Esquerda
        if factor > 1 and current.left and key < current.left.value:
            return self._rotate_right(current)

        # Direita-Direita
        if factor < -1 and current.right and key > current.right.value:
            return self._rotate_left(current)

        # Esquerda-Direita
        if factor > 1 and current.left and key > current.left.value:
            current.left = self._rotate_left(current.left)
            return self._rotate_right(current)
        # Direita-Esquerda
        if factor < -1 and current.right and key < current.right.value:
            current.right = self._rotate_right(current.right)
            return self._rotate_left(current)

        return current


    
    


