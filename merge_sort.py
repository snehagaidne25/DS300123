def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array in half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort the left and right halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Merge the sorted halves
    result = []
    i = j = 0
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            result.append(left_sorted[i])
            i += 1
        else:
            result.append(right_sorted[j])
            j += 1
    result += left_sorted[i:]
    result += right_sorted[j:]
    
    return result

unsorted_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = merge_sort(unsorted_arr)
print(sorted_arr) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]