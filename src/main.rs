mod sort;
fn main() {
    println!("Hello, world!");
    let mut a = vec![1,3,4,5,6,3,5,6,2,5,7];
    sort::quick::quick(&mut a);
    println!("sorted: {:?}", a);
}
