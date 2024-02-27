n=int(input("enter the size"))
arr=[]
for i in range(0,n):
    x=int(input())
    arr.append(x)
print(arr)

def mergesort(arr):
    if len(arr)>1:
        left=arr[:len(arr)//2]
        right=arr[len(arr)//2:]
    
        mergesort(left)
        mergesort(right)

        i=0
        j=0
        k=0

        while(i<len(left)and j<len(right)):
            if(left[i]<=right[j]):
               arr[k]=left[i]
               i+=1
               k+=1
            else:
               arr[k]=right[j]
               j+=1
               k+=1
        while(i<len(left)):
            arr[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            arr[k]=right[j]
            j+=1
            k+=1

mergesort(arr)
print("sorted array",arr)