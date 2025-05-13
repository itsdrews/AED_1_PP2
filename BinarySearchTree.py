from Node import Node
from BinaryTree import BinaryTree
class BinarySearchTree(BinaryTree):


    #herança de BinaryTree e override do método insert
    def insert(self,key:int,name:str):
        #insere um valor na árvore
        if self.root is None:
            print("Raizz")
            self.root = Node(key)
            self.root.set_name(name)
        else:
            print("Já tem raiz")
            self._insert_recursive(self.root,key,name)

    def _insert_recursive(self,current:Node,key:int,name:str):
        if (current.value < key):
            #print("Esquerda")
            if current.left is None:
                current.left = Node(key)
                current.left.set_name(name)
            else:
                self._insert_recursive(current.left,key,name)
        elif(current.value > key):
            #print("Direita")
            if current.right is None:
                current.right = Node(key)
                current.right.set_name(name)
            else:
                self._insert_recursive(current.right,key,name)
