
# Selection sort
# O(n^2)

array = [-10, 12, 47, 79, 56, 48, 33, 95, 51, 23, 30, 11, 85, 42, 75, 9, 77, 29, 88, 46, 80, 16, 35, 94, 67, 69, 65, 76, 28, 55, 97, 43, 91, 26, 96, 74, 15, 64, 22, 92, 25, 17, 39, 54, 4, 34, 87, 68, 40, 62, 1, 58, 10, 13, 89, 98, 60, 86, 84, 57, 36, 83, 90, 18, 49, 38, 6, 41, 20, 32, 7, 66, 71, 78, 19, 45, 37, 27, 100, 14, 3, 61, 73, 81, 2, 5, 72, 82, 99, 24, 8, 53, 59, 44, 52, 93, 50, 21, 31, 63]



def selection_sort(array):
    # Looping through the whole array one by one
    for i in range(len(array) - 1):

        # initalize min to the first element 
        min = i

        # Looping through the array starting with ith element
        for j in range(i + 1, len(array)):
            
            # Finding the index of the minimum value in the unsorted portion of the array
            if array[j] < array[min]: min = j

        # Optimization check (if min == i no swap is needed)
        if min != i:
            array[i], array[min] = array[min], array[i]
    
    return array
            

            
print(selection_sort(array))