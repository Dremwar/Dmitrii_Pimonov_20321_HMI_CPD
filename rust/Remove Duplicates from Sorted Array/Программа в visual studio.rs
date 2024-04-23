use std::io;
use std::io::BufRead;
fn remove_duplicates(nums: &mut Vec<i32>) -> usize {
    if nums.is_empty() {
        return 0;
    }
    
    let mut index = 0;
    
    for i in 1..nums.len() {
        if nums[i] != nums[index] {
            index += 1;
            nums[index] = nums[i];
        }
    }
    
    nums.truncate(index + 1);
    
    nums.len()
}

fn main() {
    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
    let mut nums: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let unique_count = remove_duplicates(&mut nums);
    
    println!("Unique count: {}", unique_count);
    println!("Unique elements: {:?}", nums);
}