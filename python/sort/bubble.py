# This is Bubble sort.
# Worst: O(n^2)
# Best: O(n)
# Average: O(n^2)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        isswapped  = False
        for j in range(1, n - i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                isswapped = True
        if not isswapped:
            break