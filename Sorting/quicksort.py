n=int(input("enter the size"))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
print(arr)

def quick(arr,low,high):
    if low<high:
        p=part(arr,low,high)
        quick(arr,low,p-1)
        quick(arr,p+1,high)
        #print(p)

def part(arr,low,high):
    i=low
    j=high-1
    pivot=arr[high]
    while i<j:
        while i<high and arr[i]<pivot:
            i+=1
        while j>low and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[high],arr[i]=arr[i],arr[high]
    return i

quick(arr,0,n-1)
print("sorted array",arr)