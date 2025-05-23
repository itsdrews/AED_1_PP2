from BinarySearchTree import BinarySearchTree
from Node import Node



class AVLTree(BinarySearchTree):
    def __init__(self):
        self.root = None
    def get_height(self,node:Node):
        return node.height if node else 0

    def get_balance(self,node:Node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

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
    def _balance(self,current:Node):
        # Atualiza a altura do atual
        self._update_height(current)

        # Calcula o fator de balanceamento
        factor = self.get_balance(current)

        # Esquerda-Esquerda
        if factor > 1 and current.left and current.value < current.left.value:
            return self._rotate_right(current)

        # Direita-Direita
        if factor < -1 and current.right and current.value > current.right.value:
            return self._rotate_left(current)

        # Esquerda-Direita
        if factor > 1 and current.left and current.value > current.left.value:
            current.left = self._rotate_left(current.left)
            return self._rotate_right(current)
        # Direita-Esquerda
        if factor < -1 and current.right and current.value < current.right.value:
            current.right = self._rotate_right(current.right)
            return self._rotate_left(current)
        return current

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


        return self._balance(current)

    def remove(self,key:int):

        node = self.search(key)
        if node[0] is None:
            print("Não é possível remover este nó (inexistente)")
            return None

        self.root = self._remove_recursive(self.root,key)

    def _remove_recursive(self,subtree:Node,key:int):
        if subtree is None:
            return None
        if key < subtree.value:
            subtree.left = self._remove_recursive(subtree.left,key)
        elif key > subtree.value:
            subtree.right = self._remove_recursive(subtree.right,key)
        else:
            # Caso 1: Nó sem filhos
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None:
                return subtree.right
            elif subtree.right is None:
                return subtree.left
            else:
                sucessor = self.find_sucessor(subtree.right)
                subtree.value = sucessor.value
                subtree.right = self._remove_recursive(subtree.right,sucessor.value)


        return self._balance(subtree)
    
    


