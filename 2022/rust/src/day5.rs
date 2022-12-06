use std::collections::{BTreeMap, VecDeque};

fn parse_crates(input: &Vec<String>) -> BTreeMap<String, VecDeque<char>> {
    let mut crates = BTreeMap::new();

    for line in input {
        let mut col = 0;
        let chars = line.chars().collect::<Vec<_>>();

        let mut index = 0;

        while index < chars.len() {
            if index % 4 == 0 {
                col += 1;
            }
            let entry = crates.entry(col.to_string()).or_insert(VecDeque::new());
            let c = chars[index];
            if c == '[' {
                entry.push_back(chars[index + 1]);
            }
            index += 1;
        }
    }
    crates
}

pub fn part1() -> String {
    let mut crates: BTreeMap<String, VecDeque<char>> = BTreeMap::new();
    let input = crate::util::get_input_lines("input/day5.txt");
    let mut lines = vec![];

    for line in input {
        if line.is_empty() {
            crates = parse_crates(&lines);
        } else if line.chars().next().unwrap() != 'm' {
            lines.push(line);
        } else {
            let tokens = line.split_ascii_whitespace().collect::<Vec<_>>();
            let (count, source, destination): (i32, i32, i32) = (
                tokens[1].parse().unwrap(),
                tokens[3].parse().unwrap(),
                tokens[5].parse().unwrap(),
            );
            // TODO this loop is the only difference between part1 and part2
            for _ in 0..count {
                let mut s = crates.get_mut(&source.to_string()).unwrap();
                let c = s.pop_front().unwrap();
                s = crates.get_mut(&destination.to_string()).unwrap();
                s.push_front(c);
            }
        }
    }
    let mut result = Vec::with_capacity(crates.len());
    for (_, value) in crates.into_iter() {
        result.push(value.front().unwrap().to_string());
        // result.insert(0, (value.front().unwrap()).to_string());
    }

    result.join("")
}

pub fn part2() -> String {
    let mut crates: BTreeMap<String, VecDeque<char>> = BTreeMap::new();
    let input = crate::util::get_input_lines("input/day5.txt");
    let mut lines = vec![];

    for line in input {
        if line.is_empty() {
            crates = parse_crates(&lines);
        } else if line.chars().next().unwrap() != 'm' {
            lines.push(line);
        } else {
            let tokens = line.split_ascii_whitespace().collect::<Vec<_>>();
            let (count, source, destination): (i32, i32, i32) = (
                tokens[1].parse().unwrap(),
                tokens[3].parse().unwrap(),
                tokens[5].parse().unwrap(),
            );
            let mut to_move = VecDeque::new();
            let mut s = crates.get_mut(&source.to_string()).unwrap();
            for _ in 0..count {
                let c = s.pop_front().unwrap();
                to_move.push_front(c);
            }
            for c in to_move {
                s = crates.get_mut(&destination.to_string()).unwrap();
                s.push_front(c);
            }
        }
    }
    let mut result = Vec::with_capacity(crates.len());
    for (_, value) in crates.into_iter() {
        result.push(value.front().unwrap().to_string());
    }

    result.join("")
}
