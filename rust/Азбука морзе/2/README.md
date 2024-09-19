# Dremwar_Rust
Задание: Написать программу распознающую код морзе 


# Описание программы морзе_код:
Данная программа получает на вход строку с кодем морзе, после этого она разделяет эту строку на слова и буквы и обратно соеденяет расщифрованное сообщение.


# Листинг морзе_код:
```rs
mod preloaded; //Импорт модуля preloaded, содержащего словарь морзе.
use preloaded::MORSE_CODE; //импорт Morse
use std::collections::HashMap; //Импорт HashMap


fn decode_morse(encoded: &str) -> String {//Объявление функции decode_  , которая принимает закодированную строку и возвращает раскодированное сообщение
    let a: Vec<&str> = encoded.trim().split("   ").collect();//создание вектора с разделёнными словами
    let mut d_m = Vec::new(); //создание вектора с раскодироваными словами

    for word in a {
        let m_l: Vec<&str> = word.split(' ').collect();// Разделение каждого слова на отдельные символы
        let d_w: String = m_l// Раскодирование каждой буквы и сборка их в строку 'd_w'.
            .iter()
            .map(|&letter| MORSE_CODE.get(letter).unwrap_or(&"".to_string()).to_string())
            .collect();
        d_m.push(d_w); //соеденяем буквы в слова и добавляем их в один массив.
    }

    d_m.join(" ")
}
```
Скриншот1(прохождене теста):

![alt text](image.png)

Скриншот2(Результат работы):

![alt text](image.png)


