import numpy as np

from validator import *
from person import *
from data import *

import matplotlib.pyplot as plt

def dataLoad(path):
    file = open(path)
    f = file.readlines()
    f.pop(0) # tirar a primeira linha do comentario

    lista = list()
    extremos = {
        "idade" : {
            "max" : float('-inf'),
            "min" : float('inf')
        },
        "colesterol": {
            "max" : float('-inf'),
            "min" : float('inf')
        }
    }

    for line in f:
        line = line.replace("\n", "")
        lines = line.split(",")

        if len(lines) == 6:
            if validar_inteiro(lines[0]) and validar_sexo(lines[1]) and validar_inteiro(lines[2]) and validar_inteiro(lines[3]) and validar_inteiro(lines[4]) and validar_bit(lines[5]):
                idade = int(lines[0])
                sexo = lines[1]
                tensao = int(lines[2])
                colesterol = int(lines[3])
                batimento = int(lines[4])
                doenca = bool(int(lines[5]))

                lista.append(Pessoa(idade, sexo, tensao, colesterol, batimento, doenca))

                if idade > extremos["idade"]["max"]:
                    extremos["idade"]["max"] = idade
                elif idade < extremos["idade"]["min"]:
                    extremos["idade"]["min"] = idade
                
                if colesterol > extremos["colesterol"]["max"]:
                    extremos["colesterol"]["max"] = colesterol
                elif colesterol < extremos["colesterol"]["min"]:
                    extremos["colesterol"]["min"] = colesterol 
                    
    file.close()

    return Dados(lista, extremos)


def genderDistribution(dados):
    res = {
        "M" : {
            False : 0,
            True: 0
        },
        "F" : {
            False : 0,
            True : 0
        }
    }

    for pessoa in dados.lista:
        res[pessoa.sexo][pessoa.doenca] += 1

    return res


def ageDistribution(dados):
    max = dados.extremos["idade"]["max"]

    res = dict()    
    for i in range(0,(max//5)+1):
        res[(i*5, i*5 + 4)] = {
            False : 0,
            True : 0
        }
    
    for pessoa in dados.lista:
        intervalo = pessoa.idade//5
        res[(intervalo*5, intervalo*5 + 4)][pessoa.doenca] += 1

    return res


def colesterolDistribution(dados):
    min = dados.extremos["colesterol"]["min"]
    max = dados.extremos["colesterol"]["max"]

    res = dict()
    for i in range(min//10, (max//10)+1):
        res[(i*10, i*10 + 9)] = {
            False : 0,
            True : 0
        }

    for pessoa in dados.lista:
        intervalo = pessoa.colesterol//10
        res[(intervalo*10, intervalo*10 + 9)][pessoa.doenca] += 1

    return res


def distributionTable(distribuicao):
    # Define a tabela como uma lista de listas
    tabela = [["", "Com doença", "Sem doença"]]
    
    for key in distribuicao.keys():
        tabela += [[str(key), str(distribuicao[key][True]), str(distribuicao[key][False])]]

    # Define o número de colunas e linhas da tabela
    num_colunas = len(tabela[0])
    num_linhas = len(tabela)

    # Define a largura das colunas
    larguras = [max(len(tabela[i][j]) for i in range(num_linhas)) for j in range(num_colunas)]

    # Imprime a tabela
    for i in range(num_linhas):
        for j in range(num_colunas):
            print("{:{}}".format(tabela[i][j], larguras[j]), end="  ")
        print()

def distribution_to_graph(distribution, flag):
    x_axis = np.arange(len(distribution.keys()))
    x_coordinates = [str(elem) for elem in distribution.keys()]
    y_cd = [elem[True] for elem in distribution.values()]
    y_sd = [elem[False] for elem in distribution.values()]

    plt.figure(figsize=[12, 9])

    plt.barh(x_axis - 0.2, y_cd, label="Com doença", tick_label=x_coordinates, height=0.4, color="yellow")
    plt.barh(x_axis + 0.2, y_sd, label="Sem doença", tick_label=x_coordinates, height=0.4, color="black")

    plt.yticks(x_axis, distribution.keys())
    plt.xlabel("Frequência")

    for i, v in enumerate(y_cd):
        if v != 0:
            plt.text(v, i - 0.2, " " + str(v), color='black', va='center', fontsize='xx-small')

    for i, v in enumerate(y_sd):
        if v != 0:
            plt.text(v, i + 0.2, " " + str(v), color='black', va='center', fontsize='xx-small')

    match flag:
        case 0:
            plt.title("Distribuição por género")
        case 1:
            plt.title("Distribuição por idade")
        case 2:
            plt.title("Distribuição por colesterol")

    plt.legend()
    plt.show()

def main():

    dados = dataLoad("myheart.csv")
    
    print("Como pretende que sejam apresentadas as distribuições?\n")
    print("1 - Formato Textual")
    print("2 - Formato Gráfico")

    res = input()

    if res == '1':
        print("\nDistribuição da doença por sexo:")
        distributionTable(genderDistribution(dados))
        print("\nDistribuição da doença por escalões etários:")
        distributionTable(ageDistribution(dados))
        print("\nDistribuição da doença por níveis de colesterol:")
        distributionTable(colesterolDistribution(dados))

    elif res == '2':
        print("Qual distribuição pretende visualizar em formato gráfico?")
        print("1 - Distribuição da doença por sexo")
        print("2 - Distribuição da doença por escalões etários")
        print("3 - Distribuições da doença por níveis de colesterol")
        print("4 - Sair")

        r = 0

        while r != 4:
            r = int(input())

            if r == 1:
                distribution_to_graph(genderDistribution(dados), 0)
            elif r == 2:
                distribution_to_graph(ageDistribution(dados), 1)
            elif r == 3:
                distribution_to_graph(colesterolDistribution(dados), 2)
            elif r == 4:
                print("A sair...")
            else:
                print("Opção Invalida")

if __name__ == '__main__':
    main()
