# This is Merge sort.
# Worst: O(nlogn)
# Best: O(nlogn)
# Average: O(nlogn)

def merge(arr1, arr2, left, mid, right):
    i = left
    j = mid
    k = 0
    while i < mid and j < right:
        if arr1[i] <= arr1[j]:
            arr2[k] = arr1[i]
            k += 1
            i += 1
        else:
            arr2[k] = arr1[j]
            k += 1
            j += 1
    if i == mid:
        while j < right:
            arr2[k] = arr1[j]
            k += 1
            j += 1
    else:
        while i < mid:
            arr2[k] = arr1[i]
            k += 1
            i += 1
    for l in range(k):
        arr1[left + l] = arr2[l]

def merge_sort(arr1, arr2, left, right):
    if left == right or left == right - 1:
        return
    mid = (left + right) // 2
    # sort left side
    merge_sort(arr1, arr2, left, mid)
    # sort right side
    merge_sort(arr1, arr2, mid, right)
    # connect left and right
    merge(arr1, arr2, left, mid, right)
