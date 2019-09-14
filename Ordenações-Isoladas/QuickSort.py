def partition(array, start, end):
    follower = leader = start
    while leader < end:
        if array[leader] <= array[end]:
            array[follower], array[leader] = array[leader], array[follower]
            follower += 1
        leader += 1
    array[follower], array[end] = array[end], array[follower]
    return follower

def _quicksort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    _quicksort(array, start, p-1)
    _quicksort(array, p+1, end)
    
def quicksort(array):
    _quicksort(array, 0, len(array)-1)
    
array = [8, 7, 5, 3, 1, 2, 9, 6, 4]
quicksort(array)
print("quicksort :", array)