n=int(input("enter the size"))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
print(arr)


def bubble_sort(arr):
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

bubble_sort(arr)
print("Sorted array",arr)


