use std::collections::HashMap;
use std::io;

fn main() {
    let mut company: HashMap<String, Vec<String>> = HashMap::new();

    loop {
        println!("Enter command (Add [name] to [department] OR List [department/company] OR Exit):");
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let input = input.trim();

        if input.to_lowercase() == "exit" {
            break;
        }

        let parts: Vec<&str> = input.split_whitespace().collect();

        if parts.len() >= 4 && parts[0].to_lowercase() == "add" && parts[2].to_lowercase() == "to" {
            let name = parts[1].to_string();
            let department = parts[3].to_string();
            let employees = company.entry(department.clone()).or_insert(Vec::new());
            employees.push(name);
            employees.sort();
        } else if parts.len() >= 2 && parts[0].to_lowercase() == "list" {
            if parts[1].to_lowercase() == "company" {
                for (department, employees) in company.iter() {
                    println!("{}:", department);
                    for employee in employees {
                        println!("{}", employee);
                    }
                }
            } else {
                let department = parts[1].to_string();
                match company.get(&department) {
                    Some(employees) => {
                        println!("{}:", department);
                        for employee in employees {
                            println!("{}", employee);
                        }
                    },
                    None => println!("Department not found"),
                }
            }
        } else {
            println!("Invalid command, please try again");
        }
    }
}