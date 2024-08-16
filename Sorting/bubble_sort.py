
# Bubble sort
# O(n^2)


array = [70, -12, 47, 79, 56, 48, 33, 95, 51, 23, 30, 11, 85, 42, 75, 9, 77, 29, 88, 46, 80, 16, 35, 94, 67, 69, 65, 76, 28, 55, 97, 43, 91, 26, 96, 74, 15, 64, 22, 92, 25, 17, 39, 54, 4, 34, 87, 68, 40, 62, 1, 58, 10, 13, 89, 98, 60, 86, 84, 57, 36, 83, 90, 18, 49, 38, 6, 41, 20, 32, 7, 66, 71, 78, 19, 45, 37, 27, 100, 14, 3, 61, 73, 81, 2, 5, 72, 82, 99, 24, 8, 53, 59, 44, 52, 93, 50, 21, 31, 63]


def bubble_sort(array):
    # Outer loop: controls the number of passes through the array
    for i in range(len(array) - 1):

        # Inner loop: compares adjacent elements, range shrinks with each pass
        for j in range(len(array) - i - 1):

            # if current element is greater than the next one -> swap
            if array[j] > array[j + 1]:

                # swap operation
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
        
print(bubble_sort(array))