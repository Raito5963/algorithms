# This is Quick sort.
# Worst: O(n^2)
# Best: O(nlogn)
# Average: O(nlogn)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    # arr[1:] : all elements except pivot
    low = [i for i in arr[1:] if i <= pivot]
    high = [i for i in arr[1:] if i > pivot]
    
    return quick_sort(low) + [pivot] + quick_sort(high)

# There are two algorithms of partition.

# Lomuto partition (simple)
def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

# Hoare partition (few swap and stable)
def hoare_partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

# This quick sort is in-place with Hoare partition.
def quick_sort_inplace(arr, low, high):
    if low >= high:
        return
    
    p = hoare_partition(arr, low, high)
    quick_sort_inplace(arr, low, p)
    quick_sort_inplace(arr, p+1, high)