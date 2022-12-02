use std::cmp;

use crate::util::get_input_lines;

pub fn part1() -> i32 {
    let mut maximum = 0;
    let mut current = 0;

    for line in get_input_lines("input/day1.txt") {
        if line.is_empty() {
            current = 0;
            continue;
        }
        current += line.parse::<i32>().unwrap();
        maximum = cmp::max(current, maximum);
    }
    maximum
}

pub fn part2() -> i32 {
    let mut current = 0;
    let mut counts = Vec::new();

    for line in get_input_lines("input/day1.txt") {
        if line.is_empty() {
            counts.push(current);
            current = 0;
            continue;
        }
        current += line.parse::<i32>().unwrap();
    }

    counts.push(current);
    counts.sort();
    println!("{:?}", counts);
    counts.iter().rev().take(3).sum()
}
