from BinarySearchTree import BinarySearchTree
from Node import Node
from BinaryTree import BinaryTree


class AVLTree(BinarySearchTree):

    def insert(self,node:Node):
        #herda o insert de BST e insere o nó
        super().insert(node)

        #herda o nó raiz do BinarySearchTree
        root = super(BinaryTree).root

        #atualiza a altura do nó
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        #fator de balanceamento
        balance = self.get_balance(root)

        if balance < 1 and node.value < root.left.value:
            self.rotate_right(root)
        if balance < -1 and node.value > root.right.value:
            self.rotate_left(root)
        if balance > 1 and node.value > root.left.value:
            root.left = self.rotate_left(root.left)
            self.rotate_right(root)
        if balance < -1 and node.value < root.right.value:
            root.right = self.rotate_right(root.right)
            self.rotate_left(root)












    def get_height(self,node:Node):
        return self.get_height if node else 0

    def get_balance(self,node:Node):
        return abs(self.get_height(node.left) - self.get_height(node.right)) if node else 0

    def rotate_right(self,node:Node):
        print(f"Rodação á direita do {node.to_string()}")

        x = node.left
        T2 = x.right

        x.right = node
        node.left = T2

        self.update_height(x)
        self.update_height(node)

        return node

    def rotate_left(self,node:Node):
        print(f"Rodação á esquerda do {node.to_string()}")
        x = node.right
        T2 = x.left

        x.left = node
        node.right = T2

        self.update_height(x)
        self.update_height(node)

        return node

    def update_height(self,node:Node):
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))