# This is Radix sort.
# Worst: O(k * n) # k: digits

# 4bit radix for int
def radix_sort(arr: list[int]):
    if not arr:
        return arr
    
    max_val = max(arr)
    if max_val == 0:
        return arr
    
    # 4bit shift and sort
    shift = 0
    while (max_val >> shift) > 0:
        # buckets for hex(0~15)
        buckets = [[] for _ in range(16)]

        for elem in arr:
            # Get current digit of hex.
            digit = (elem >> shift) & 0xf
            buckets[digit].append(elem)

        # decode into list
        arr = [elem for bucket in buckets for elem in bucket]

        # next hex
        shift += 4
    return arr
    