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
        print(f"Rodação á direita do {y.to_string()}")

        x = y.left
        aux = x.right

        x.right = y
        y.left = aux

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self,x:Node):
        print(f"Rodação á esquerda do {x.to_string()}")
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

        #rotacionando para esquerda
        if factor>1:
            if self.get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        #rotacionando para esquerda
        if factor<-1:
            if self.get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    #Override na função de inseração recursiva adicionando balanceamento
    def _insert_recursive(self,current:Node,key:str,name:str):
        print(f"inserindo{key} nome {name}")
        if (current.value > key):
            print("Esquerda")
            if current.left is None:
                current.left = Node(key)
                current.left.set_name(name)
            else:
                self._insert_recursive(current.left,key,name)
        elif(current.value < key):
            print("Direita")
            if current.right is None:
                current.right = Node(key)
                current.right.set_name(name)
            else:
                self._insert_recursive(current.right,key,name)


        return self._balance(current)

