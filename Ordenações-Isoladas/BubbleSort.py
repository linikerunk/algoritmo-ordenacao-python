# algoritmo BubbleSort feito por Liniker ....
##################################INICIO########################################
'''
Exemplo esse Algoritmo Percorre o Array fazendo a troca com o adjacente se maior \
ele realiza a troca, ele é um algoritmo que funciona muito bem se o array já estiver
ordenado, ele é o pior algortimo para ordenação..
    '''
def BubbleSort(array):
    for final in range(len(array), 0, -1):
        troca = False

        for atual in range(0, final - 1):
            if array[atual] > array[atual + 1]:
                array[atual + 1], array[atual] = array[atual], array[atual + 1]
                troca = True

        if not troca:
            break
 # Aqui rolou eu faço a troca..
                

if __name__ == '__main__':
    array = [8, 7, 5, 3, 1, 2, 9, 6, 4]
    BubbleSort(array)
    print("BubbleSort :", array)
