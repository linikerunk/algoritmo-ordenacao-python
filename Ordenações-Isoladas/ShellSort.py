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


nlist = [14,46,43,27,57,41,45,21,70]
ShellSort(nlist)
print(nlist)