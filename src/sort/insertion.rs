// This is Insertion sort.
// Worst: O(n^2)
// Best: O(n)
// Average: O(n^2)

// It is simple and easy to implement.
// also, it is fast with small array.
// stable, in-place, online algorithm.

pub fn insertion<T: Ord + Copy>(arr: &mut Vec<T>){
    // Copy
    // It can copy a value to other variables
    let n = arr.len();
    for i in 1..n {
        if arr[i-1] > arr[i] {
            let mut j = i;
            let temp = arr[i];
            while j > 0 && arr[j-1] > temp {
                arr[j] = arr[j-1];
                j -= 1;
            }
            arr[j] = temp;
        }
    }
}