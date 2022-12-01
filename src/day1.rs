use std::cmp;
use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn part1() -> i32 {
    let file = File::open("input/day1.txt").unwrap();
    let reader = BufReader::new(file);
    let mut maximum = 0;
    let mut current = 0;

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for line in reader.lines() {
        let line = line.unwrap(); // Ignore errors.
                                  // Show the line and its number.
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
    let file = File::open("input/day1.txt").unwrap();
    let reader = BufReader::new(file);
    let mut current = 0;
    let mut counts = Vec::new();

    for line in reader.lines() {
        let line = line.unwrap();
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
