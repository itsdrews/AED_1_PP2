import csv
import time

from AVLTree import AVLTree
from Node import Node
from BinaryTree import BinaryTree
from BinarySearchTree import BinarySearchTree

FILE_NAME = "./src/cidades.csv"
def get_data(FILE_NAME):
    data = []
    with open(FILE_NAME, newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            line = list(line)
            data.append(line)

    return data

def create_binary_tree(arr):

    binary_tree = BinaryTree()
    for i in range(len(arr)):
        key = arr[i][0]
        name = arr[i][1]
        binary_tree.insert(key,name)
    return binary_tree

def create_binary_search_tree(arr):
    binary_search_tree = BinarySearchTree()
    for i in range(len(arr)):
        key = arr[i][0]
        name = arr[i][1]
        binary_search_tree.insert(key,name)
        print(f" valor: {key} {name}")
    return binary_search_tree

def create_avl_tree(arr):
    avl_tree = AVLTree()
    for i in range(len(arr)):
        key = arr[i][0]
        name = arr[i][1]
        avl_tree.insert(key,name)

    return avl_tree
def main():

    # Para ver o tempo do algoritmo : start = time.time()

    # Pegando os dados do arquvio
    file_data = get_data(FILE_NAME)
    file_data.pop(0) #removendo os nomes das colunas

    #**************************************************************

    #criando árvore binária genérica e aleatória
    #binary_tree = create_binary_tree(file_data) #passando o nó raiz e o vetor para ser setado
    #traverse pre fixado
    #binary_tree.pre_order_traversal()

    #**************************************************************
    #criando árvore binária de busca
    #binary_search_tree = create_binary_search_tree(file_data)
    #traverse pre fixado
    #binary_search_tree.pre_order_traversal()

    #**************************************************************
    #criando árvore avl
    avl_tree = create_avl_tree(file_data)
    #traverse pre fixado
    avl_tree.pre_order_traversal()


if __name__ == '__main__':
    main()

