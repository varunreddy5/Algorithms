def merge(left,right):
    result=[]
    i,j = 0,0
    while(i<len(left) and j<len(right)):
        if(left[i] <= right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result

def mergesort(lst):
    if(len(lst)<=1):
        return lst
    mid = int(len(lst)/2)
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    return merge(left,right)

print(mergesort([2,4,1,6,8,5,3,7]))
