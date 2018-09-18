def quick_sort(arr,start,end):
    if start<end:
        pivot_index = partition(arr,start,end)
        quick_sort(arr, start, pivot_index-1)
        quick_sort(arr, pivot_index+1, end)
    return arr

def partition(arr,start,end):
    pivot=end
    pindex = start
    for i in range(start, end):
        if arr[i] < arr[pivot]:
            arr[pindex],arr[i] = arr[i], arr[pindex]
            pindex+=1
    arr[pindex],arr[pivot] = arr[pivot],arr[pindex]
    return pindex

arr=[7,2,1,6,8,5,3,4]
print(quick_sort(arr, 0, len(arr)-1))
