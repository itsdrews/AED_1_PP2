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

    def search(self,key:int):
        comparisons = {'count': 0}
        result = self._search_recursive(self.root,key,comparisons)
        return result,comparisons

    #Override do método search com uma pequena diferença (distinção entre maior e menor)
    def _search_recursive(self,subtree:Node,key:int,comparisons):
        if subtree is None:
            return None
        comparisons['count'] += 1
        if int(subtree.value) == int(key):
            return subtree
        elif int(key) < int(subtree.value):
            return self._search_recursive(subtree.left,key,comparisons)
        else:
            return self._search_recursive(subtree.right,key,comparisons)