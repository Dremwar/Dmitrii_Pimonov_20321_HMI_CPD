use std::io;
fn main() {
    let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess);

    let length = guess.len();
    
    let a = guess.split(" ");
    
    let mut length2=0;
    for part in a {
    length2 = part.len();
    }
    println!("{:#?}",length2-2); 

}

