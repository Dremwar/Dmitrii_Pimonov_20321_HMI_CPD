use std::io;
fn fibonacci(n: u32) -> u64 {
    if n == 0 {
        return 0;
    } else if n == 1 {
        return 1;
    } else {
        let mut prev = 0;
        let mut current = 1;
        for _ in 2..=n {
            let tmp = prev + current;
            prev = current;
            current = tmp;
        }
        return current;
    }
}

fn main() {
    let mut input2 = String::new();
    io::stdin().read_line(&mut input2)
        .expect("Не удалось прочитать строку");
    let n: u32 = input2.trim().parse()
        .expect("Введено некорректное число");
    let result = fibonacci(n);
    println!("{:?}", result);
}