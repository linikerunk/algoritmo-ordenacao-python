# algoritmo MergeSort feito por Liniker ....
'''
Esse algoritmo funciona da seguinte forma dividir para conquistar, ele divide o array
por metades quando ele tem uma unica porça ele começa a fazer o merge desse array..
exemplo 10 indice, divide por 2 : <-5 \ 5 -> merge no da esquerda depois merge no da direita
e no final merge nos 10 elementos
OBS: Complexidade Algoritma Logaritma  (n\log n) 
'''

from time import sleep

def MergeSort(array):
    ordena_metade(array, 0, len(array) - 1)


def ordena_metade(array, inicio, fim):
    if inicio >= fim:
        return

    meio = (inicio + fim) // 2 # divisão de Inteiros ...

    ordena_metade(array, inicio, meio)# do inicio até o meio...
    ordena_metade(array, meio + 1, fim)# do meio + 1 até o final...

    merge(array, inicio, fim)


def merge(array, inicio, fim):
    array[inicio: fim + 1] = sorted(array[inicio: fim + 1])


import random
import time

array = [random.randint(0, 1000000) for i in range(1000000)]
inicio = time.time()
MergeSort(array)
sleep(50)

'''
fim = time.time()
print(fim - inicio)
'''
