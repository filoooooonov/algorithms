
# Binary search
# O(log(n))


array = [5, 7, 6, 2, 9, 8]
array.sort()

def binary_search(array, target):
    lo = 0
    hi = len(array) - 1
    
    # while the array has more than 1 element
    while lo <= hi:
        mid_ind = (lo + hi) // 2
        
        if array[mid_ind] == target:
            return True
        
        # right hand side
        elif array[mid_ind] < target:
            lo = mid_ind + 1
    
        # left hand side
        elif array[mid_ind] > target:
            hi = mid_ind -1 
        
    return False    
        


print(binary_search(array, 2))


