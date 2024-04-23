impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
                return String::new();
            }
            
            let mut prefix = String::new();
            for i in 0..strs[0].len() {
                let char = strs[0].chars().nth(i).unwrap();
                for j in 1..strs.len() {
                    if i >= strs[j].len() || char != strs[j].chars().nth(i).unwrap() {
                        return prefix;
                    }
                }
                prefix.push(char);
            }
            prefix
    }
}