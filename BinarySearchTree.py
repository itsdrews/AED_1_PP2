from Node import Node
from BinaryTree import BinaryTree
class BinarySearchTree(BinaryTree):


    #herança de BinaryTree e override do método insert
    def insert(self,key:int,name:str):
        #para o primeiro nó
        self.root = self._insert_recursive(self.root,key,name)

    def _insert_recursive(self,current:Node,key:int,name:str):
        if current is None:
            new_node = Node(key)
            new_node.set_name(name)
            return new_node
        
        if key < current.value:
            current.left = self._insert_recursive(current.left,key,name)
        elif key > current.value:
            current.right = self._insert_recursive(current.right,key,name)
        else:
            pass

        return current