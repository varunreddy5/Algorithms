def selection_sort(arr):
    n= len(arr)
    for i in range(0,n-1):
        imin=i
        for j in range(i+1,n):
            if(arr[j]<arr[imin]):
                imin=j
        temp=arr[imin]
        arr[imin]=arr[i]
        arr[i]=temp
    return arr
print(selection_sort([11,18,0,7,8,9,1,2,5,10,3,6]))
