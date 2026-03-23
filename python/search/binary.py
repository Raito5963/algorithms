# This is Binary search.
# Worst: O(logn)
# Best: O(1)
# Average: O(logn)

# An array must be sorted beforehand.

def binary_search(arr, target):
    n = len(arr)
    l = 0
    r = n - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            return m
    return None