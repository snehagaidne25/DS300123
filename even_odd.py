no = int(input("Enter a Number:"))

i = 1
even_cnt = 0
odd_cnt = 0
while i <= no:
    if(i % 2 == 0):
        even_cnt += 1
    else:
        odd_cnt += 1
    i += 1

print("number of even numbers:", even_cnt)
print("number of even numbers:", odd_cnt)


'''
Output:

Enter a Number : 9
number of even numbers: 4
number of odd numbers: 5

'''