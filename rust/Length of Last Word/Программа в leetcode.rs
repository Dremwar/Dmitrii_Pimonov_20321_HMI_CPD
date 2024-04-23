impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let last_word_length = match s.split_whitespace().last() {
        Some(last_word) => last_word.len(),
        None => 0,
        };
        return(last_word_length as i32) 
    }
}