# This is Linear search.
# Worst: O(n)
# Best: O(1)
# Average: O(n)

def linear_search(arr,target):
    n = len(arr)
    for idx in range(n):
        if arr[idx] == target:
            return idx
    return None