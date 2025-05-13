from BinarySearchTree import BinarySearchTree
from Node import Node
from BinaryTree import BinaryTree


class AVLTree(BinarySearchTree):
    def get_height(self,node:Node):
        return self.get_height if node else 0

    def get_balance(self,node:Node):
        return abs(self.get_height(node.left) - self.get_height(node.right)) if node else 0

    def _rotate_right(self,node:Node):
        print(f"Rodação á direita do {node.to_string()}")

        x = node.left
        T2 = x.right

        x.right = node
        node.left = T2

        self.update_height(x)
        self.update_height(node)

        return node

    def _rotate_left(self,node:Node):
        print(f"Rodação á esquerda do {node.to_string()}")
        x = node.right
        T2 = x.left

        x.left = node
        node.right = T2

        self.update_height(x)
        self.update_height(node)

        return node

    def _update_height(self,node:Node):
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))
    def _balance(self,node:Node,node2:Node):
        factor = self.get_balance(node)

        #rotacionar para direita
        if factor >1 and node2.value < node.left.value:
            return self._rotate_right(node)
        #rotacionar para a esquerda
        if factor < -1 and node2.value > node.right.value:
            return self._rotate_left(node)
        if factor > 1 and node2.value > node.left.value:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if factor < -1 and node2.value < node.right.value:
            node.right = self._rotate_right(node)
            return self._rotate_left(node)

        return node

    def _insert_recursive(self,current:Node,node:Node):
        if node.value < current.value:
            current.left = self._insert_recursive(current.left,node)
        elif node.value > current.value:
            current.right = self._insert_recursive(current.right,node)
        else:
            return node

        self._update_height(node)
        return self._balance(current,node.value)