
# Quick sort
# O(nlog(n))


import random

array = [7, 1, 9, 3, 2, 8, 5]
array = [8, 2, 4, 7, 1, 3, 9, 6, 5]


random.seed("ABC")
array = [random.randint(0, 1000) for _ in range(0, 100)]


def quick_sort(array, start, end):

    # Base case
    if end <= start:
        return False
    
    
    pivot = partition(array, start, end)
    # Recursion: quicksort the two parts of the array excluding the pivot
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)


# return the index of the pivot
def partition(array, start, end):
    pivot = array[end]
    # i is 1 step behind the start of the array
    i = start - 1


    
    j = start
    while j <= end - 1:

        # compare jth element and the pivot
        if array[j] < pivot:
            i += 1
            # swap i and j
            array[i], array[j] = array[j], array[i]
        j += 1
    i += 1

    # put the pivot back in place?
    array[i], array[end] = array[end], array[i]
    return i


quick_sort(array, 0, len(array) - 1)
print(array)

