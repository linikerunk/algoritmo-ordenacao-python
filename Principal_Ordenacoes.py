#ALGORITMO DE ORDENAÇÕES PARA O TRABALHO DE COMPUTABILIDADE E COMPLEXIDADE DE ALGORITMOS
# AUTHOR: LINIKER OLIVEIRA  - CEUNSP (SALTO)


import random
import time
import sys
import sys
x=1500
sys.setrecursionlimit(x)

def BubbleSort(vetor):
    for final in range(len(vetor), 0, -1):
        troca = False

        for atual in range(0, final - 1):
            if vetor[atual] > vetor[atual + 1]:
                vetor[atual + 1], vetor[atual] = vetor[atual], vetor[atual + 1]
                troca = True

        if not troca:
            break

def SelectionSort(vetor):
    for indice in range(0, len(vetor)):
        min_indice = indice

        for direita in range(indice + 1, len(vetor)):
            if vetor[direita] < vetor[min_indice]: # pois precisamos encontrar o menor elemento da direita
                min_indice =  direita # se ele for menor ele virá o menor indice
            
        vetor[indice], vetor[min_indice] = vetor[min_indice], vetor[indice] # Aqui eu faço a troca...

def InsertionSort(vetor):
    for posicao in range(0, len(vetor)):
        elemento_atual = vetor[posicao]

        while posicao > 0 and vetor[posicao - 1] > elemento_atual:
            vetor[posicao] = vetor[posicao - 1]
            posicao -= 1

        vetor[posicao] = elemento_atual


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


def ShellSort(lista):
    sublista = len(lista)//2
    while sublista > 0:
      for posicao_inicial in range(sublista):
        faz_InsertionSort(lista, posicao_inicial, sublista)

      sublista = sublista // 2

def faz_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        valor_atual = nlist[i]
        posicao = i

        while posicao>=gap and nlist[posicao-gap]>valor_atual:
            nlist[posicao]=nlist[posicao-gap]
            posicao = posicao-gap

        nlist[posicao]=valor_atual

def BucketSort(array):
    k = max(array)
    bucket = [0]* (k+1)
    for j in range(len(array)):
        bucket[array[j]] = bucket[array[j]] + 1
    indice = 0
    for i in range(k+1):
        for j in range(bucket[i]):
            array[indice] = i
            indice = indice + 1


def QuickSort(array):
    less = []
    equal = []
    greater = []
    # print array
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        less = QuickSort(less)
        greater = QuickSort(greater)
        return greater + equal + less


vetor = []
numeros_gerados = False
opcao = True
numeros_dados = int(input(" Digite o tamanho de dados que vc quer ordenar : "))
while (opcao != 0):
    print('\t','*' * 20, '\
    \t MENU','\t','*'*20,)
    opcao = int(input('\t 0 - Sair  \n \
    \t 1 - Imprimir Vetor  \n\
    \t 2 - Gerar Vetor  \n \
    \t 3 - Organizar Vetor Ordem Decrescente \n \
    \t 4 - Organizar o Vetor Ordem Crescente \n \
    \t 5 - BubbleSort \n \
    \t 6 - SelectionSort \n \
    \t 7 - InsertionSort \n \
    \t 8 - MergeSort  \n \
    \t 9 - ShellSort \n \
    \t 10 - BucketSort \n \
    \t 11 - QuickSort \n \
    \t Opção : '))

    if int(opcao) == 0:
        exit(1)
    elif int(opcao) == 1:
        if numeros_gerados == True:
            print('\n IMPRIMIR O VETOR \n')
            for v in vetor:
                print("Vetor ["+ str(v) +"]")
        else:
            print("Antes de imprimir o vetor, gere os números aleatórios através da opção '2'")
                
    elif int(opcao) == 2:
        vetor = [random.randint(0, numeros_dados) for i in range(numeros_dados)]
        numeros_gerados = True
                    
    elif int(opcao) == 3:
        if numeros_gerados == True:
            vetor = (sorted(vetor, reverse = True))
        else:
            print(' Erro. Primeiro gere o vetor.')

    elif int(opcao) == 4:
        if numeros_gerados == True:
            vetor = (sorted(vetor))
        else:
            print(' Erro. Primeiro gere o vetor.')

    elif int(opcao) == 5:
        if numeros_gerados == True:
            print("\t [Método BubbleSort] Ordenando Vetores \t")
            inicio = time.time()
            BubbleSort(vetor)
            fim = time.time()
            tempototal = fim - inicio
            print(f"Início = {inicio:.2f} Segundos")
            print(f"Fim = {fim:.2f} Segundos")
            print(f"Tempo Total = {tempototal:.2f}")
            print(f" A Ordenação levou {tempototal:.2f} Segundos")
        else:
            print(' Erro. Primeiro gere o vetor.')
    elif int(opcao) == 6:
        if numeros_gerados == True:
            print("\t [Método SelectionSort] Ordenando Vetores \t")
            inicio = time.time()
            SelectionSort(vetor)
            fim = time.time()
            tempototal = fim - inicio
            print(f"Início = {inicio:.2f} Segundos")
            print(f"Fim = {fim:.2f} Segundos")
            print(f"Tempo Total = {tempototal:.2f}")
            print(f" A Ordenação levou {tempototal:.2f} Segundos")
        else:
            print(' Erro. Primeiro gere o vetor.')
    elif int(opcao) == 7:
        if numeros_gerados == True:
            print("\t [Método InsertionSort] Ordenando Vetores \t")
            inicio = time.time()
            InsertionSort(vetor)
            fim = time.time()
            tempototal = fim - inicio
            print(f"Início = {inicio:.2f} Segundos")
            print(f"Fim = {fim:.2f} Segundos")
            print(f"Tempo Total = {tempototal:.2f}")
            print(f" A Ordenação levou {tempototal:.2f} Segundos")
        else:
            print(' Erro. Primeiro gere o vetor.')
    elif int(opcao) == 8:
        if numeros_gerados == True:
            print("\t [Método MergeSort] Ordenando Vetores \t")
            inicio = time.time()
            MergeSort(vetor)
            fim = time.time()
            tempototal = fim - inicio
            print(f"Início = {inicio:.2f} Segundos")
            print(f"Fim = {fim:.2f} Segundos")
            print(f"Tempo Total = {tempototal:.2f}")
            print(f" A Ordenação levou {tempototal:.2f} Segundos")
        else:
            print(' Erro. Primeiro gere o vetor.')
    elif int(opcao) == 9:
        if numeros_gerados == True:
            print("\t [Método ShellSort] Ordenando Vetores \t")
            inicio = time.time()
            ShellSort(vetor)
            fim = time.time()
            tempototal = fim - inicio
            print(f"Início = {inicio:.2f} Segundos")
            print(f"Fim = {fim:.2f} Segundos")
            print(f"Tempo Total = {tempototal:.2f}")
            print(f" A Ordenação levou {tempototal:.2f} Segundos")
        else:
            print(' Erro. Primeiro gere o vetor.')

    elif int(opcao) == 10:
        if numeros_gerados == True:
            print("\t [Método BucketSort] Ordenando Vetores \t")
            inicio = time.time()
            BucketSort(vetor)
            fim = time.time()
            tempototal = fim - inicio
            print(f"Início = {inicio:.2f} Segundos")
            print(f"Fim = {fim:.2f} Segundos")
            print(f"Tempo Total = {tempototal:.2f}")
            print(f" A Ordenação levou {tempototal:.2f} Segundos")
        else:
            print(' Erro. Primeiro gere o vetor.')
    elif int(opcao) == 11:
        if numeros_gerados == True:
            print("\t [Método QuickSort] Ordenando Vetores \t")
            inicio = time.time()
            QuickSort(vetor)
            fim = time.time()
            tempototal = fim - inicio
            print(f"Início = {inicio:.2f} Segundos")
            print(f"Fim = {fim:.2f} Segundos")
            print(f"Tempo Total = {tempototal:.2f}")
            print(f" A Ordenação levou {tempototal:.2f} Segundos")
        else:
            print(' Erro. Primeiro gere o vetor.')
    else:
        print("Opção inválida, digite novamente...")
    
 
        


        

