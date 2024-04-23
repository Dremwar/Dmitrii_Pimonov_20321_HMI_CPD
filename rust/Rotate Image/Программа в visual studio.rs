fn rotate_image(matrix: &mut Vec<Vec<i32>>) {
    let n = matrix.len();

    for i in 0..n/2 {
        for j in i..n-i-1 {
            let temp = matrix[i][j];
            matrix[i][j] = matrix[n-j-1][i];
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1];
            matrix[n-i-1][n-j-1] = matrix[j][n-i-1];
            matrix[j][n-i-1] = temp;
        }
    }
}

fn main() {
    let mut image = vec![vec![1,2,3], vec![4,5,6], vec![7,8,9]];
    
    println!("Original image:");
    for row in &image {
        println!("{:?}", row);
    }

    rotate_image(&mut image);

    println!("Rotated image:");
    for row in &image {
        println!("{:?}", row);
    }
}