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
        key = int(arr[i][0])
        name = arr[i][1]
        binary_tree.insert(key,name)
    return binary_tree

def create_binary_search_tree(arr):
    binary_search_tree = BinarySearchTree()
    for i in range(len(arr)):
        key = int(arr[i][0])
        name = arr[i][1]
        binary_search_tree.insert(key,name)
    return binary_search_tree

def create_avl_tree(arr):
    avl_tree = AVLTree()
    for i in range(len(arr)):
        key = int(arr[i][0])
        name = arr[i][1]
        avl_tree.insert(key,name)

    return avl_tree

def check_result(result,comp):
    if result:
        print(f"Valor encontrado! Nome associado: {result.name}, ID: {result.value}")
        print(f"Número de comparações: {comp['count']}")
    else:
        print("Valor não encontrado")
        print(f"Número de comparações: {comp['count']}")


def main():



    # Pegando os dados do arquvio
    file_data = get_data(FILE_NAME)
    file_data.pop(0) #removendo os nomes das colunas

    #**************************************************************

    # Para ver o tempo do algoritmo :
    start = time.time()
    # Criando árvore binária genérica e aleatória
    binary_tree = create_binary_tree(file_data) #passando o nó raiz e o vetor para ser setado
    # Traversal pre fixado
    # Binary_tree.pre_order_traversal()
    # Search para ID 100084,Moreira Verde
    result,comp = binary_tree.search(100084)
    print("Search para Árvore Binária Aleatória: ")
    check_result(result,comp)
    finish = time.time()
    print(f"Tempo para criação e busca em Árvore Binária Aleatória: {finish-start:.15f}")
    print("*" *30)

    #**************************************************************
    # Criando árvore binária de busca
    start = time.time()
    binary_search_tree = create_binary_search_tree(file_data)
    # Traversal pre fixado
    #binary_search_tree.pre_order_traversal()
    # Search para ID 10084, Moreira Verde
    result,comp = binary_search_tree.search(100084)
    print("Search para Árvore Binária de Busca: ")
    check_result(result,comp)
    finish = time.time()
    print(f"Tempo para criação e busca em Árvore Binária de Busca: {finish-start:.12f}")
    print("*" *30)
    #**************************************************************
    # Criando árvore avl
    start = time.time()
    avl_tree = create_avl_tree(file_data)
    # Traversal pre fixado
    #avl_tree.pre_order_traversal()
    result, comp = avl_tree.search(100084)
    print("Search para Árvore AVL: ")
    check_result(result, comp)
    finish = time.time()
    print(f"Tempo para criação e busca em Árvore Binária AVL: {finish-start:.12f}")
    print("*" *30)

    #todo adicionar exclusão
    #todo adicionar retorno de traversal por lista para visualizar



if __name__ == '__main__':
    main()

