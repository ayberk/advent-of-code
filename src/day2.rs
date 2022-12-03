use crate::util::get_input_lines;

struct Hand {
    ours: Plays,
    theirs: Plays,
}

#[derive(Copy, Clone)]
enum Plays {
    Rock,
    Paper,
    Scissors,
    Unknown,
}

fn process_hand(hand: &Hand) -> i32 {
    let mut points = 0;

    points += match hand.ours {
        Plays::Rock => 1,
        Plays::Paper => 2,
        Plays::Scissors => 3,
        _ => 0,
    };

    points += match (hand.ours, hand.theirs) {
        (Plays::Rock, Plays::Rock) => 3,
        (Plays::Paper, Plays::Paper) => 3,
        (Plays::Scissors, Plays::Scissors) => 3,
        (Plays::Rock, Plays::Scissors) => 6,
        (Plays::Paper, Plays::Rock) => 6,
        (Plays::Scissors, Plays::Paper) => 6,
        (_, _) => 0,
    };

    points
}

fn parse_play(us: &str, them: &str) -> Hand {
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

    Hand { ours: a, theirs: b }
}

pub fn part1() -> i32 {
    let mut total = 0;

    // Read the file line by line using the lines() iterator from std::io::BufRead.
    for line in get_input_lines("input/day2.txt") {
        let mut played = line.split_whitespace();
        let them = played.next().unwrap();
        let us = played.next().unwrap();
        let hand = parse_play(us, them);
        total += process_hand(&hand);
    }
    total
}

pub fn part2() -> i32 {
    for line in get_input_lines("input/day2.txt") {
        let mut played = line.split_whitespace();
        let them = played.next().unwrap();
        let us = played.next().unwrap();

        let new_us = if us == "X" {
            // lose
            match them {
                "A" => "Z",
                "B" => "X",
                "C" => "Y",
                _ => "",
            }
        } else if us == "Y" {
            match them {
                // draw
                "A" => "X",
                "B" => "Y",
                "C" => "Z",
                _ => "",
            }
        } else {
            match them {
                "A" => "Y",
                "B" => "Z",
                "C" => "X",
                _ => "",
            }
        };

        let hand = parse_play(new_us, them);

        total += process_hand(&hand);
    }
    total
}
