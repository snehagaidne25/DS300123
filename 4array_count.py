def count_pairs_with_given_sum(arr, target):
    count = {}
    pairs = 0

    
    for num in arr:
        diff = target - num
        if diff in count:
            pairs += count[diff]
        if num not in count:
            count[num] = 0
        count[num] += 1

count_pairs_with_given_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)