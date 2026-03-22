// This is Bubble sort.
// Worst: O(n^2)
// Best: O(n)
// Average: O(n^2)

fn bubble<T: Ord>(arr: &mut Vec<T>){
    // <T: Ord>
    // <T> is generics and means no tyoe has been specified.
    // <Ord> is Order and restricted to types who can assign an order.
    // &mut Vec<T>
    // It means reference to Vec that is mutable
    let mut n = arr.len() // Python: n = len(arr)
    for i in 0..n {
        let mut isswapped = false
        for j in 1..n - i{
            if arr[j] < arr[j-1]{
                arr.swap(j, j - 1)
                isswapped = true
            }
        }
        if !isswapped { break; }
    }
}
