def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        value = arr[i]
        hole = i
        while(hole>0 and arr[hole-1]>value):
            arr[hole]=arr[hole-1]
            hole=hole-1
        arr[hole]=value
    return arr
print(insertion_sort([7,2,4,1,5,3]))    
