import csv
import time
from Node import Node
from BinaryTree import BinaryTree

FILE_NAME = "./src/cidades.csv"
def get_data(FILE_NAME):
    data = []
    with open(FILE_NAME, newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            line = list(line)
            data.append(line)

    return data
def main():

    # Para ver o tempo do algoritmo : start = time.time()

    # Pegando os dados do arquvio
    file_data = get_data(FILE_NAME)
    file_data.pop(0) #removendo os nomes das colunas
    root = Node(file_data[0][0])
    root.set_name(file_data[0][1])#primeiro valor a ser inserido

    file_data.pop(0) # removendo a raiz do vetor com valores

    #setando a raiz da árvore binária
    binary_tree = BinaryTree(root)
    print(binary_tree.root.to_string())
    for i in range(len(file_data)):

        node = Node(file_data[i][0])
        node.set_name(file_data[i][1])









    # Abrindo o arquvio e obtendo as linhas




if __name__ == '__main__':
    main()

