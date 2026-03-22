// This is Quick sort.
// Worst: O(n^2)
// Best: O(nlogn)
// Average: O(nlogn)

// There are two algorithms of partition

// Lomuto Partition (simple)
fn lomuto<T: Ord>(arr: &mut [T]) -> usize {
    let high = arr.len() - 1;
    let mut i = 0;
    for j in 0..high {
        if arr[j] <= arr[high] {
            arr.swap(i, j);
            i += 1;
        }
    }
    arr.swap(i, high);
    i
}

// Hoare Partition (few swap)
fn hoare<T: Ord + Copy>(arr: &mut [T]) -> usize {
    let pivot = arr[arr.len() / 2];
    let mut i = 0;
    let mut j = arr.len() - 1;

    loop {
        while arr[i] < pivot { i += 1; }
        while arr[j] > pivot { j -= 1; }
        if i >= j { return j; }
        arr.swap(i, j);
        i += 1;
        j -= 1;
    }
}

//  This quick sort is in-place with Hoare partition.
fn quick_sort<T: Ord + Copy>(arr: &mut [T]) {
    if arr.len() <= 1 { return; }

    let p = hoare(arr); 

    let (left, right) = arr.split_at_mut(p + 1);
    quick_sort(left);
    quick_sort(right);
}