# This is Heap sort.
# Worst: O(nlogn)
# Best: O(n)
# Average: O(nlogn)

# unstable sort

def heapify(arr, n, i):
    largest = i # parent node
    left = 2 * i + 1 # left child
    right = 2 * i + 2 # right child

    #　Update if left child is bigger than parent.
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Update if right child is bigger than parent.
    if right < n and arr[right] > arr[largest]:
        largest = right

    # if parent node is not maximum, change and adjust recursively.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Change array into heap (create maximum heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # The largest element in the heap is extracted 
    # and the array is sorted by swapping it with the last element.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) # adjust other heap