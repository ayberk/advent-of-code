use std::collections::HashSet;

use crate::util::get_input_lines;

fn find_common_element(a: &str, b: &str) -> char {
    let set_b = b.chars().collect::<HashSet<_>>();
    let set_a = a.chars().collect::<HashSet<_>>();

    *set_a.intersection(&set_b).collect::<Vec<_>>()[0]
}

fn find_common_element2(a: &Vec<String>) -> char {
    let set1 = a[0].chars().collect::<HashSet<_>>();
    let set2 = a[1].chars().collect::<HashSet<_>>();
    let set3 = a[2].chars().collect::<HashSet<_>>();

    let intersection = set1.intersection(&set2).collect::<HashSet<_>>();
    let intersection2 = set3.intersection(&set2).collect::<HashSet<_>>();
    **intersection
        .intersection(&intersection2)
        .collect::<Vec<_>>()[0]
}

fn get_priority(c: char) -> i32 {
    let is_lower = 'a' <= c && c <= 'z';

    if is_lower {
        c as i32 - 'a' as i32 + 1
    } else {
        c as i32 - 'A' as i32 + 27
    }
}

pub fn part1() -> i32 {
    let mut total = 0;
    for line in get_input_lines("input/day3.txt") {
        let (head, tail) = line.split_at(line.len() / 2);
        let common = find_common_element(head, tail);
        total += get_priority(common);
    }
    total
}
pub fn part2() -> i32 {
    let mut total = 0;
    let mut buffer: Vec<String> = vec![];
    for line in get_input_lines("input/day3.txt") {
        buffer.push(line);
        if buffer.len() == 3 {
            let common = find_common_element2(&buffer);
            total += get_priority(common);
            buffer.clear();
        }
    }
    total
}
