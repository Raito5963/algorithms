# This is Tim sort.
# Worst: O(nlogn)
# Best: O(n)
# Average: O(nlogn)

# def tim_sort(arr: list):
#   return arr.sort()

# min run is minimum number of elements of sub array
# There are 2 conditions
# 1. (len(arr) / min_run) ≒ 2^n
# 2.  8 < min_run < 256
# The best min_run is 32~64

def calc_min_run(n):
    r = 0
    while n >= 64:
        r |= n & 1
        # right shift n 
        n >>= 1
    return n + r

# insertion sort and merge sort for tim sort.
def insertion_tim(arr, l, r):
    for i in range(l+1, r+1):
        j = i
        while j > l and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

def merge_tim(arr, l, m, r):
    left = arr[l : m + 1]
    right = arr[m + 1 : r + 1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def tim_sort(arr):
    n = len(arr)
    min_run = calc_min_run(n)
    for i in range(0, n, min_run):
        # Prevent out of bounds access to the list
        end = min(i + min_run - 1, n - 1)
        insertion_tim(arr, i, end)
    size = min_run
    while size < n:
        # Get left index of merging two arrays 
        for left in range(0, n, 2 * size):
            # Get middle index of merging two arrays
            mid = min(n - 1, left + size - 1)
            # Get right index of merging two arrays
            right = min((left + 2 * size - 1), n - 1)
            if mid < right and arr[mid] > arr[mid+1]: 
                merge_tim(arr, left, mid, right)
        size = 2 * size
