def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[len(arr)//2]
    left=[x for x in arr if x<pivot]
    mittle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quicksort(left)+mittle+quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))