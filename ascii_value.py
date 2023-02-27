#program to creat a dictionary of alphabets and their ASCII values

alphabets = "abcdefghijklmnopqrstuvwxyz"
ascii_value = {alphabet : ord(alphabet)for alphabet in alphabets}
print(ascii_value)
