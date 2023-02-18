from validator import *
from pessoa import *
from dados import *

import matplotlib.pyplot as plt
import networkx as nx 

def carregar_dados(path):
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


def distribuicao_sexo(dados):
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


def distribuicao_etaria(dados):
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


def distribuicao_colesterol(dados):
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


def tabela_distribuicao(distribuicao):
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

def main():

    dados = carregar_dados("myheart.csv")
    
    print("Como pretende que sejam apresentadas as distribuições?\n")
    print("1 - Formato Textual")
    print("2 - Formato Gráfico")

    res = input()

    if res == '1':
        print("\nDistribuição da doença por sexo:")
        tabela_distribuicao(distribuicao_sexo(dados))
        print("\nDistribuição da doença por escalões etários:")
        tabela_distribuicao(distribuicao_etaria(dados))
        print("\nDistribuição da doença por níveis de colesterol:")
        tabela_distribuicao(distribuicao_colesterol(dados))

    elif res == '2':
        res = distribuicao_sexo(dados)

        labels = ['M','F']
        vals = [int(res['M'][True]),int(res['F'][True])]

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(labels, vals)
        plt.show()

    

    #tabela_distribuicao(distribuicao_etaria(dados))
    #print("\n")
    #tabela_distribuicao(distribuicao_colesterol(dados))

if __name__ == '__main__':
    main()
