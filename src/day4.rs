use crate::util::get_input_lines;

pub fn does_contain(a: (i32, i32), b: (i32, i32)) -> bool {
    (a.0 <= b.0 && a.1 >= b.1) || (b.0 <= a.0 && b.1 >= a.1)
}

pub fn does_overlap(a: (i32, i32), b: (i32, i32)) -> bool {
    !(b.0 > a.1 || a.0 > b.1)
}

pub fn process_elf(coverage: &str) -> (i32, i32) {
    let mut split = coverage.split('-');
    let first = split.next().unwrap();
    let second = split.next().unwrap();

    (first.parse().unwrap(), second.parse().unwrap())
}

pub fn part1() -> i32 {
    let mut total = 0;
    for line in get_input_lines("input/day4.txt") {
        let mut split = line.split(',');
        let first = process_elf(split.next().unwrap());
        let second = process_elf(split.next().unwrap());
        if does_contain(first, second) {
            total += 1
        }
    }
    total
}

pub fn part2() -> i32 {
    let mut total = 0;
    for line in get_input_lines("input/day4.txt") {
        let mut split = line.split(',');
        let first = process_elf(split.next().unwrap());
        let second = process_elf(split.next().unwrap());
        if does_overlap(first, second) {
            total += 1
        }
    }
    total
}
