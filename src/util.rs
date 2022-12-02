use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn get_input_lines(filename: &str) -> Vec<String> {
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    let mut lines = Vec::new();

    for line in reader.lines() {
        let line = line.unwrap();
        lines.push(line);
    }

    lines
}
