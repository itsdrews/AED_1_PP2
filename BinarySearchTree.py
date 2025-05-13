from Node import Node
from BinaryTree import BinaryTree
class BinarySearchTree(BinaryTree):


    #herança de BinaryTree e override do método insert
    def insert(self,node: Node):
        #insere um valor na árvore
        if self.root is None:
            print("Raizz")
            self.root = Node(node.value)
            self.root.set_name(node.name)
        else:
            print("Já tem raiz")
            self._insert_recursive(self.root,node)

    def _insert_recursive(self,current:Node,node:Node):
        if (current.value < node.value):
            #print("Esquerda")
            if current.left is None:
                current.left = node
            else:
                self._insert_recursive(current.left,node)
        elif(current.value > node.value):
            #print("Direita")
            if current.right is None:

                current.right = node
            else:
                self._insert_recursive(current.right,node)

        return node