def insertion_sort(arr):
    # Loop through each element in the array
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements that are greater than the key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key into its correct position
        arr[j + 1] = key
        
    return arr


unsorted_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = insertion_sort(unsorted_arr)
print(sorted_arr) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]