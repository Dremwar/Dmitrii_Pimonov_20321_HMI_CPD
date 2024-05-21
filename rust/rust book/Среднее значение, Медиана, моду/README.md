# Dremwar_CPD
Задание: Container With Most Water (Вам задан целочисленный массив height длиной n. Проведено n вертикальных линий таким образом, что две конечные точки i-й строки равны (i, 0) и (i, высота[i]).
Найдите две линии, которые вместе с осью x образуют контейнер, таким образом, чтобы в контейнере было больше всего воды.
Укажите максимальное количество воды, которое может вместиться в контейнер.
Обратите внимание, что вы не можете наклонять контейнер.)


# Описание программы Container With Most Water:
Данная прога принимает строку из высот барикад контейнера и рассчитывает максимальное количество воды помещёное в контейнер и выводит его.


# Листинг Container With Most Water:
```rs
Программа в leetcode
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
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
}
```

```rs
программа в visual studio
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
```

Скриншот1(Результат работы):

![alt text](image.png)


