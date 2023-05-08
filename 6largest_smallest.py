a=[]
n= int(input ("Enter the number of elements: "))
print("Enter the array elements")
for i in range(0,n):
    a.append(int(input()))
k= int(input("Ener the value of k: "))
l=int(input("Enter 1 for kTh largest or 0 for kth smallest: "))


for i in range(0,n):
    for j in range(0, n-i-1):
        if(a[j]>a[j+1]):
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t

print("\nThe sorted elements:",end=" ")
for i in range(0,n):
    print(a[i], end=" ")


if l==1:
    for i in range(n-1, n-k-1, -1):
        m=0
    print("\nThe ",k, "th largest element is: ",a[i])

else:
    for i in range(0,k):
        m=0
    print("\nThe ",k, "th smallest element is: ",a[i])
