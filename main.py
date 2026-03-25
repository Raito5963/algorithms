import time
import random
from python.sort.bubble import bubble_sort

def make_dummy(n=100000):
    return [random.randint(0,65535) for _ in range(n)]

if __name__ == "__main__":
    print(f"Generating 100,000 elements...")
    arr = make_dummy()

    print("Start sorting...")
    start = time.time()
    arr.sort()
    end = time.time()
    print(f"Done! Elapsed time:{end - start:.5f} sec")