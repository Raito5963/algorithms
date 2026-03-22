# This is Selection sort.
# Worst: O(n^2)
# Best: O(n^2)
# Average: O(n^2)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        temp = i
        for j in range(i+1, n):
            if arr[j] < arr[temp]:
                temp = j
        arr[i], arr[temp] = arr[temp], arr[i]