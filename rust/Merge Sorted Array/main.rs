use std::io;
use std::io::BufRead;
fn main() {

    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
    let mut nums1: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let mut input1 = String::new();
    io::stdin().read_line(&mut input1)
        .expect("Не удалось прочитать строку");

    let m: usize = input1.trim().parse()
        .expect("Введено некорректное число");

    nums1.truncate(m);
    
    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
    let mut nums2: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let mut input2 = String::new();
    io::stdin().read_line(&mut input2)
        .expect("Не удалось прочитать строку");

    let n: usize = input2.trim().parse()
        .expect("Введено некорректное число");

    nums2.truncate(n);

    nums1.append(&mut nums2);
    nums1.sort();
    println!("{:?}", nums1);
}


