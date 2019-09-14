# algoritmo SelectionSort feito por Liniker ....
'''
O algortimo de SelectionSort ele percorre o Array fazendo uma verificação se naquele
laço ele seleciona o primeiro indice e percorre o array até encontrar o menor item de um 
array para fazer a troca, esse algoritmo não precisa de mémoria extra para fazer ordenação
ele nao precisa de um array auxiliar..., porém se os números de elementos for grande
ele aplicará de forma quadratica..

OBS = Complexidade do algoritmo Quadratica O(n)^2
'''

def SelectionSort(array):
    for indice in range(0, len(array)):
        min_indice = indice

        for direita in range(indice + 1, len(array)):
            if array[direita] < array[min_indice]: # pois precisamos encontrar o menor elemento da direita
                min_indice =  direita # se ele for menor ele virá o menor indice
            
        array[indice], array[min_indice] = array[min_indice], array[indice] # Aqui eu faço a troca...

array = [9, 8, 7, 3, 4, 2, 1]
SelectionSort(array)
print(array)
