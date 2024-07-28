
# Merge sort
# O(nlog(n))


import random

array = [5, 6, 1, 4, 2, 9, 3]

random.seed("ABC")
array = [random.randint(0, 1000) for _ in range(0, 100)]


def merge_sort(array):

    # Base case: if array has only 1 element it is already sorted
    if len(array) > 1:

        # Create sub arrays
        mid_ind = len(array) // 2
        left_array = array[:mid_ind]
        right_array = array[mid_ind:]

        # Sort the two arrays recursively
        merge_sort(left_array)
        merge_sort(right_array)

        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index
        
        # Merge the sorted arrays into the original array
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        # If there are remaining elements in the left_array, add them to the original array
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        # If there are remaining elements in the right_array, add them to the original array
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1


merge_sort(array)
print(array)