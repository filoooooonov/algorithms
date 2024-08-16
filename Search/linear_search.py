
# Linear search
# O(n)

array = [6, 5, 4, 9, 8, 3]

# Iterate through each element and compare it with the target
def linear_search(array, target):
    for i in range(len(array)):
        if (array[i] == target):
            return True
        
    return False

print(linear_search(array, 5))