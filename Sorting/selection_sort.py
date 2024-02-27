n=int(input("enter the size"))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
print(arr)


def selection_sort(arr):
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j

        arr[i],arr[min]=arr[min],arr[i]

selection_sort(arr)
print("Sorted array",arr)


