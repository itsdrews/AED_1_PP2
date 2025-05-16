import csv
import time

from astropy.table import BST

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
        data.pop(0)
    return data

def create_tree(type,arr):
    if type == "AVL":
        tree = AVLTree()
    elif type == "BST":
        tree = BinarySearchTree()
    else:
        tree = BinaryTree()

    for i in range(len(arr)):
        key = int(arr[i][0])
        name = arr[i][1]
        tree.insert(key,name)

    return tree


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

    #**************************************************************

    # Para ver o tempo do algoritmo :
    start = time.time()
    # Criando árvore binária genérica e aleatória
    binary_tree = create_tree("BINARY",file_data)
    # Traversal pre fixado
    # binary_tree.pre_order_traversal()

    # Search para ID 100084,Moreira Verde
    print("Search para Árvore Binária Aleatória: ")

    result,comp = binary_tree.search(100084)
    check_result(result,comp)

    #Remove para AB aleatória
    binary_tree.remove(100084)
    result,comp = binary_tree.search(100084)
    check_result(result,comp)

    finish = time.time()
    print(f"Tempo para criação e busca em Árvore Binária Aleatória: {finish-start:.15f} segundos")
    print("*" *30)


    #**************************************************************
    # Criando árvore binária de busca
    start = time.time()

    binary_search_tree = create_tree("BST",file_data)

    # Traversal pre fixado
    #binary_search_tree.pre_order_traversal()

    # Search para ID 10084, Moreira Verde
    print("Search para Árvore Binária de Busca: ")

    result,comp = binary_search_tree.search(100084)
    check_result(result,comp)

    # Remove para ABB
    binary_search_tree.remove(100084)
    result,comp = binary_search_tree.search(100084)
    check_result(result,comp)


    finish = time.time()
    print(f"Tempo para criação e busca em Árvore Binária de Busca: {finish-start:.15f} segundos")
    print("*" *30)
    #**************************************************************
    start = time.time()

    # Criando árvore avl
    avl_tree = create_tree("AVL",file_data)

    # Traversal pre fixado
    #avl_tree.pre_order_traversal()

    print("Search para Árvore AVL: ")

    result, comp = avl_tree.search(100084)
    check_result(result, comp)

    # Remove para AVL
    avl_tree.remove(100084)
    result,comp = avl_tree.search(100084)
    check_result(result,comp)



    finish = time.time()
    print(f"Tempo para criação e busca em Árvore Binária AVL: {finish-start:.15f} segundos")
    print("*" *30)

    #todo adicionar exclusão
    #todo adicionar retorno de traversal por lista para visualizar



if __name__ == '__main__':
    main()

