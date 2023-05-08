def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element
    pivot = arr[len(arr) // 2]
    
    # Partition the array into sub-arrays based on the pivot element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # Recursively sort the sub-arrays
    return quick_sort(left) + middle + quick_sort(right)

unsorted_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = quick_sort(unsorted_arr)
print(sorted_arr) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]