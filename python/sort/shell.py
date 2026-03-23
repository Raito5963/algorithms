# This is Shell sort.
# Worst: Addict with distance
# Best: O(nlogn)
# Average: Addict with distance

# 1. Determine an appropriate interval.
# 2. Apply insertion sort to the data sequence extracted at interval
# 3. Narrow the interval and repeat step 2.
# 4. When h=1, apply insertion sort one last time to finish.

def shell(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            # Do insertion sort with interval gap.
            while j - gap >= 0 and arr[j] < arr[j-gap]:
                arr[j], arr[j-gap] = arr[j-gap], arr[j]
                j -= gap
        # After sortion once, halve the gap and sort again.
        gap //= 2