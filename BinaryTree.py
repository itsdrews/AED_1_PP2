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


    def _pre_order_recursive(self,subtree:Node):
        if subtree is not None:
            print(subtree.to_string())
            self._pre_order_recursive(subtree.left)
            self._pre_order_recursive(subtree.right)



    def in_order_traversal(self):
        self._in_order_recursive(self.root)
    def _in_order_recursive(self,subtree:Node):
        if subtree is not None:
            self._in_order_recursive(subtree.left)
            print(subtree.to_string())
            self._in_order_recursive(subtree.right)


    def post_order_traversal(self):
        self._post_order_recursive(self.root)

    def _post_order_recursive(self,subtree:Node):
        if subtree is not None:
            self._post_order_recursive(subtree.left)
            self._post_order_recursive(subtree.right)
            print(subtree.to_string())

    def search(self):
        return self._search_recursive(self.root,value)

    def _search_recursive(self):
