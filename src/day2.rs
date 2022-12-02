use std::{
    collections::HashMap,
    fs::File,
    io::{BufRead, BufReader},
}; // 1.3.0

struct Hand {
    ours: String,
    theirs: String,
}

struct Hand2 {
    ours: Plays,
    theirs: Plays,
}

#[derive(Hash, Eq, PartialEq)]
enum Plays {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
    Unknown = 4,
}

fn process_hand(hand: &Hand) -> i32 {
    let mut points = 0;

    points += match hand.ours.as_str() {
        "X" => 1,
        "Y" => 2,
        "Z" => 3,
        _ => 0,
    };

    println!("first : {}", points);

    if hand.ours.eq(hand.theirs.as_str()) {
        points += 3;
        println!("second : {}", points);
    } else {
        let (a, b) = (hand.ours.as_str(), hand.theirs.as_str());
        points += match (a, b) {
            ("Y", "A") => 6,
            ("Z", "B") => 6,
            ("X", "C") => 6,
            ("X", "A") => 3,
            ("Y", "B") => 3,
            ("Z", "C") => 3,
            (_, _) => 0,
        };
        println!("third : {}", points);
    }

    println!("returning : {}", points);
    points
}

fn process_hand2(hand: &Hand2) -> i32 {
    let file = File::open("input/day2.txt").unwrap();
    let reader = BufReader::new(file);
    let mut total = 0;
    for line in reader.lines() {
        let line = line.unwrap();
        let mut played = line.split_whitespace();
        let them = played.next().unwrap();
        let us = played.next().unwrap();

        let a = match us {
            "X" => Plays::Rock,
            "Y" => Plays::Paper,
            "Z" => Plays::Scissors,
            _ => Plays::Unknown,
        };

        let b = match them {
            "A" => Plays::Rock,
            "B" => Plays::Paper,
            "C" => Plays::Scissors,
            _ => Plays::Unknown,
        };

        let hand = Hand {
            ours: us.to_string(),
            theirs: them.to_string(),
        };

        let winner: HashMap<Plays, Plays> = HashMap::from([
            (Plays::Rock, Plays::Scissors),
            (Plays::Paper, Plays::Rock),
            (Plays::Scissors, Plays::Rock),
        ]);
        total += process_hand(&hand);
    }
    let winner: HashMap<Plays, Plays> = HashMap::from([
        (Plays::Rock, Plays::Scissors),
        (Plays::Paper, Plays::Rock),
        (Plays::Scissors, Plays::Rock),
    ]);

    0
}

pub fn part1() -> i32 {
    let file = File::open("input/day2.txt").unwrap();
    let reader = BufReader::new(file);
    let mut total = 0;

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for line in reader.lines() {
        let line = line.unwrap();
        let mut played = line.split_whitespace();
        let them = played.next().unwrap();
        let us = played.next().unwrap();
        let hand = Hand {
            ours: us.to_string(),
            theirs: them.to_string(),
        };
        total += process_hand(&hand);
    }
    total
}

pub fn part2() -> i32 {
    let file = File::open("input/day2.txt").unwrap();
    let reader = BufReader::new(file);
    let mut total = 0;

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for line in reader.lines() {
        let line = line.unwrap();
        let mut played = line.split_whitespace();
        let them = played.next().unwrap();
        let us = played.next().unwrap();

        let mut hand = Hand {
            ours: us.to_string(),
            theirs: them.to_string(),
        };
        // rock paper scissors
        // a b c
        // x y z
        //lose draw win

        let new_ours = if us == "X" {
            // lose
            match hand.theirs.as_str() {
                "A" => "Z",
                "B" => "X",
                "C" => "Y",
                _ => "S",
            }
        } else if us == "Y" {
            match hand.theirs.as_str() {
                // draw
                "A" => "X",
                "B" => "Y",
                "C" => "Z",
                _ => "S",
            }
        } else {
            match hand.theirs.as_str() {
                "A" => "Y",
                "B" => "Z",
                "C" => "X",
                _ => "S",
            }
        };

        hand.ours = new_ours.to_string();

        total += process_hand(&hand);
    }
    total
}
