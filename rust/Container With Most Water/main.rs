use std::io;
use std::io::BufRead;
fn max_area(height: Vec<i32>) -> i32 {
    let mut max_area = 0;
    let mut left = 0;
    let mut right = height.len() - 1;
    
    while left < right {
        let h = height[left].min(height[right]);
        let w = (right - left) as i32;
        max_area = max_area.max(h * w);
        
        if height[left] < height[right] {
            left += 1;
        } else {
            right -= 1;
        }
    }
    
    max_area
}

fn main() {
    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
    let mut height: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    println!("Максимальная площадь контейнера: {}", max_area(height));
}


