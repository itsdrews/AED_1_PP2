from Node import Node
from random import choice
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,node: Node):
        #insere um valor na árvore
        if self.root is None:
            #print("Raizz")
            self.root = Node(node.value)
            self.root.set_name(node.name)
        else:
            #print("Já tem raiz")
            self._insert_recursive(self.root,node)

    def _insert_recursive(self,current:Node,node:Node):
        if choice([True, False]):
            #print("Esquerda")
            if current.left is None:
                current.left = node
            else:
                self._insert_recursive(current.left,node)
        else:
            #print("Direita")
            if current.right is None:

                current.right = node
            else:
                self._insert_recursive(current.right,node)


    def pre_order_traversal(self):
        self._pre_order_recursive(self.root)


    def _pre_order_recursive(self,node:Node):
        if node is not None:
            print(node.to_string())
            self._pre_order_recursive(node.left)
            self._pre_order_recursive(node.right)



    def in_order_traversal(self,subtree):
        if subtree:
            self.in_order_traversal(subtree.left)
            print(subtree.value +" " + subtree.name)
            self.in_order_traversal(subtree.right)
    def post_order_traversal(self,subtree):
        if subtree:
            self.post_order_traversal(subtree.left)
            self.post_order_traversal(subtree.right)
            print(subtree.value + " " + subtree.name)