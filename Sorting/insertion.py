n=int(input("enter the size"))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
print(arr)


def insertion_sort(arr):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

insertion_sort(arr)
print("Sorted array",arr)


