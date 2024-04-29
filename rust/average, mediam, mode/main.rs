use std::collections::HashMap;
use std::io;
use std::io::BufRead;

fn calculate_stats(numbers: Vec<i32>) -> (i32, i32, i32) {
    let mut sorted_numbers = numbers.clone();
    sorted_numbers.sort();

    let mean = numbers.iter().sum::<i32>() / numbers.len() as i32;
    
    let median = if numbers.len() % 2 == 0 {
        let mid = numbers.len() / 2;
        (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    } else {
        sorted_numbers[numbers.len() / 2]
    };

    let mut freq_map = HashMap::new();
    for &num in &numbers {
        *freq_map.entry(num).or_insert(0) += 1;
    }

    let mut mode = 0;
    let mut max_freq = 0;
    for (&num, &freq) in &freq_map {
        if freq > max_freq {
            max_freq = freq;
            mode = num;
        }
    }

    (mean, median, mode)
}

fn main() {
    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
    let numbers: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (mean, median, mode) = calculate_stats(numbers);

    println!("Average: {}", mean);
    println!("Median: {}", median);
    println!("Mode: {}", mode);
}