from Node import Node
from random import choice
class BinaryTree:
    def __init__(self, root:Node):
        self.root = root

    def insert(self,root:Node,node: Node):
        #insere um valor na árvore
        if root is None:
            root =Node(node.value)
        if choice([True, False]):



    def pre_order_traversal(self,subtree):
        if subtree is not None:
            print(subtree.value)
            self.pre_order_traversal(subtree.left)
            self.pre_order_traversal(subtree.right)

    def in_order_traversal(self,subtree):
        if subtree is not None:
            self.in_order_traversal(subtree.left)
            print(subtree.value)
            self.in_order_traversal(subtree.right)
    def post_order_traversal(self,subtree):
        if subtree is not None:
            self.post_order_traversal(subtree.left)
            self.post_order_traversal(subtree.right)
            print(subtree.value)