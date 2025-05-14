
from Node import Node
from random import choice
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,key:int,name:str):
        # Estabelece o valor de raiz para a árvore inteira
        self.root = self._insert_recursive(self.root,key,name)

    def _insert_recursive(self,current:Node,key:int,name:str):
        if current is None:
            new_node = Node(key)
            new_node.set_name(name)
            return new_node
        if choice([True, False]):
            # Aloca o nó na esquerda
            if current.left is None:
                current.left = Node(key)
                current.left.set_name(name)
            else:
                self._insert_recursive(current.left,key,name)
        else:
            # Aloca o nó na direita
            if current.right is None:
                current.right = Node(key)
                current.right.set_name(name)
            else:
                self._insert_recursive(current.right,key,name)
        return current

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

    def search(self,key:int):
        comparisons = {'count':0}
        result = self._search_recursive(self.root,key,comparisons)
        return result,comparisons

    def _search_recursive(self,subtree:Node,key:int,comparisons:dict):
        if subtree is None:
            return None
        comparisons['count'] += 1
        if int(subtree.value) == int(key):
            return subtree
        left_result = self._search_recursive(subtree.left,key,comparisons)
        if left_result:
            return left_result
        return self._search_recursive(subtree.right,key,comparisons)
