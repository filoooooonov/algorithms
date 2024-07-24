
# Insertion sort
# O(n^2)


array = [7, 4, 5, 9, 1, 2, 8, 3, 6]

def insertion_sort(array):

    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1

        while j >= 0 and array[j] > temp:
            array[j + 1] = array[j] 
            j -= 1
        array[j + 1] = temp


    return array


print(insertion_sort(array))