def find_duplicates(arr):
    count = {}
    duplicates = []

    # Traverse the array and count the occurrences of each element
    for num in arr:
        if num not in count:
            count[num] = 0
        count[num] += 1

    # Traverse the count dictionary and find the duplicates
    for num, freq in count.items():
        if freq > 1:
            duplicates.append(num)

    return duplicates


find_duplicates([1, 2, 3, 4, 5, 2, 7, 8, 8, 9])
