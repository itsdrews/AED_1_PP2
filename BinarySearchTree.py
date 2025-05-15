from tenacity import retry_all

from Node import Node
from BinaryTree import BinaryTree
class BinarySearchTree(BinaryTree):

    # Herança de BinaryTree 
    def insert(self,key:int,name:str):
        # Para o primeiro nó
        self.root = self._insert_recursive(self.root,key,name)

    def _insert_recursive(self,current:Node,key:int,name:str):
        # Recursiva para inseração segundo as regras de ABB
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
        # Guarda o valor das comparações 
        result = self._search_recursive(self.root,key,comparisons)
        return result,comparisons

    # Override do método search com uma pequena diferença (distinção entre maior e menor)
    def _search_recursive(self,subtree:Node,key:int,comparisons):
        if subtree is None:
            return None
        comparisons['count'] += 1
        
        if subtree.value== key:
            return subtree
        elif key < subtree.value:
            return self._search_recursive(subtree.left,key,comparisons)
        else:
            return self._search_recursive(subtree.right,key,comparisons)

    def remove(self,key:int):
        node = self.search(key)
        if node[0] is None:
            print("Não é possível remover este nó (inexistente)")
            return None

        self.root = self._remove_recursive(self.root,key)


    def _remove_recursive(self,subtree:Node,key:int):
        if subtree is None:
            return None
        if key < subtree.value:
            subtree.left = self._remove_recursive(subtree.left,key)
        elif key > subtree.value:
            subtree.right = self._remove_recursive(subtree.right,key)
        else:
            # Caso 1: Nó sem filhos
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None:
                return subtree.right
            elif subtree.right is None:
                return subtree.left
            else:
                sucessor = self.find_sucessor(subtree.right)
                subtree.value = sucessor.value
                subtree.right = self._remove_recursive(subtree.right,sucessor.value)

        return subtree

