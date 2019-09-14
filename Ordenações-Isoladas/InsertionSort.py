# algoritmo InsertionSort feito por Liniker ....
'''
O InsertionSort ele vai percorrer o vetor pegando um elemento e enquanto o item da esquerda
for maior que o elemento que ele está verificando ele vai trocar isso verificando o array como todo

OBS = Complexidade do algoritmo Quadratica O(n)^2

'''


def InsertionSort(array):
    for posicao in range(0, len(array)):
        elemento_atual = array[posicao]

        while posicao > 0 and array[posicao - 1] > elemento_atual:
            array[posicao] = array[posicao - 1]
            posicao -= 1

        array[posicao] = elemento_atual



array = [9, 7, 8, 1, 3, 5, 2, 0]
InsertionSort(array)
print(array)