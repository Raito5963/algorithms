# This is Insertion sort.
# Worst: O(n^2)
# Best: O(n)
# Average: O(n^2)

# It is simple and easy to implement.
# also, it is fast with small array.
# stable, in-place, online algorithm.

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            j = i
            temp = arr[i]
            while j > 0 and arr[j-1] > temp:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = temp