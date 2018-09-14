def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(0,n-1):
            if(arr[j+1]<arr[j]):
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
    return arr
print(bubble_sort([7,2,4,1,5,3,0,-1,-2]))
