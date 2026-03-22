// This is Selection sort.
// Worst: O(n^2)
// Best: O(n^2)
// Average: O(n^2)

fn selection<T: Ord>(arr: &mut Vec<T>){
    let n = arr.len()
    for i in 0..n{
        let mut temp = i
        for j in i + 1..n{
            if arr[j] < arr[temp]{
                temp = j
            }
        }
        arr.swap(i, temp)
    }
}