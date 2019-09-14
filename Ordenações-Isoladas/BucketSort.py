def bucket_sort(array):
    k = max(array)
    bucket = [0]* (k+1)
    for j in range(len(array)):
        bucket[array[j]] = bucket[array[j]] + 1
    indice = 0
    for i in range(k+1):
        for j in range(bucket[i]):
            array[indice] = i
            indice = indice + 1

