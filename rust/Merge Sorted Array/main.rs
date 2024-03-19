use std::io;
fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &Vec<i32>, n: i32) {
    let (mut i, mut j, mut k) = (m - 1, n - 1, (m + n - 1) as usize);
    
    while i >= 0 && j >= 0 {
        if nums1[i as usize] > nums2[j as usize] {
            nums1[k] = nums1[i as usize];
            i -= 1;
        } else {
            nums1[k] = nums2[j as usize];
            j -= 1;
        }
        k -= 1;
    }
    
    while j >= 0 {
        nums1[k] = nums2[j as usize];
        k -= 1;
        j -= 1;
    }
}

fn main() {
    
    let mut nums1 = String::new();
    io::stdin().read_line(&mut nums1)
        .expect("Не удалось прочитать строку");
    let mut nums1: Vec<i32> = nums1.trim()
        .split_whitespace()
        .map(|num| num.parse().expect("Введите корректное число"))
        .collect();

    
    let length = nums1.len();
    println!("{:#?}", length);
    let m = 3;
    let nums2 = vec![2, 5, 6];
    let n = 3;
    
    merge(&mut nums1, m, &nums2, n);
    
    println!("{:?}", nums1);
}


