my_list = ['apple', 'cat', 'bat', 'dog', 'zebra', 'banana']

reference_dict = {k: i for i, k in enumerate(sorted(set(''.join(my_list))))}


def my_key(word):
    return [reference_dict[char] for char in word]


sorted_list = sorted(my_list, key=my_key)


print(sorted_list) # Output: ['apple', 'bat', 'banana', 'cat', 'dog', 'zebra']