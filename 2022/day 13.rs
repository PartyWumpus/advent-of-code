use json;
use std::cmp;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

#[derive(PartialEq, Debug)]
enum SortedStatus {
    Yes,
    No,
    Unknown,
}

fn main() {
    part_1("./data.txt");
    part_2("./data.txt");
}

fn part_1(filename: &str) {
    let mut total = 0;
    let mut index = 1;

    let mut packet_pair: (Option<json::JsonValue>, Option<json::JsonValue>) = (None, None);
    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(data) = line {
                //println!("{data}");
                if None == packet_pair.0 {
                    packet_pair.0 = json::parse(&data).ok();
                    //println!("{:?}", packet_pair.0);
                } else if None == packet_pair.1 {
                    packet_pair.1 = json::parse(&data).ok();
                    //println!("{:?}", packet_pair.1);
                } else {
                    //println!("{:?}", packet_pair.0);
                    let result = compare_lists(&packet_pair.0.unwrap(), &packet_pair.1.unwrap());
                    if result == SortedStatus::Yes {
                        total += index
                    }

                    packet_pair = (None, None);
                    index += 1;
                }
            }
        }
    }
    println!("part 1: {total}")
}

fn part_2(filename: &str) {
    let mut all_packets: Vec<json::JsonValue> = Vec::new();
    if let Ok(lines) = read_lines(filename) {
        for line in lines {
            if let Ok(data) = line {
                let x = json::parse(&data);
                //println!("{:#?}", x);
                match x {
                    Ok(value) => all_packets.push(value),
                    _ => {},
                }
            }
        }
    }

    let mut sorted_packets: Vec<json::JsonValue> = Vec::new();
    for packet in all_packets {
      add_element_to_sorted_list(packet, &mut sorted_packets);
    }

  let val1 = add_element_to_sorted_list(json::array![[2]], &mut sorted_packets).unwrap();
  let val2 = add_element_to_sorted_list(json::array![[6]], &mut sorted_packets).unwrap();
  println!("[[2]]: {}", val1+1);
  println!("[[6]]: {}", val2+1);
  println!("part 2: {}", (val1 + 1) * (val2 + 1));
}

fn add_element_to_sorted_list(new_packet: json::JsonValue, sorted_packets: &mut Vec<json::JsonValue>) -> Option<usize> {
  let mut index = None;
  for (i, sorted_packet) in sorted_packets.iter().enumerate() {
    if compare_lists(&new_packet, sorted_packet) == SortedStatus::Yes {
      index = Some(i);
      break;
    }
  }
  match index {
    Some(i) => {sorted_packets.insert(i, new_packet)},
    None => {sorted_packets.push(new_packet)},
  }
  return index;
}


fn compare_lists(packet1: &json::JsonValue, packet2: &json::JsonValue) -> SortedStatus {
    for i in 0..cmp::max(packet1.len(), packet2.len()) {
        let val1 = &packet1[i];
        let val2 = &packet2[i];
        match val1 {
            json::JsonValue::Null => return SortedStatus::Yes, // left list ran out first, so return Yes

            json::JsonValue::Number(val1) => {
                match val2 {
                    json::JsonValue::Null => return SortedStatus::No, // right list ran out first, so return No

                    json::JsonValue::Number(val2) => {
                        if (val1.as_parts().1) < (val2.as_parts().1) {
                            return SortedStatus::Yes;
                        };
                        if (val1.as_parts().1) > (val2.as_parts().1) {
                            return SortedStatus::No;
                        };
                    }
                    json::JsonValue::Array(_) => {
                        let result = compare_lists(&json::array![val1.as_parts().1], val2);
                        if result != SortedStatus::Unknown {
                            return result;
                        };
                    }
                    _ => {
                        panic!("value is neither a list a number or a null")
                    }
                }
            }

            json::JsonValue::Array(_) => {
                match val2 {
                    json::JsonValue::Null => return SortedStatus::No, // right list ran out first, so return No

                    json::JsonValue::Number(val2) => {
                        let result = compare_lists(val1, &json::array![val2.as_parts().1]);
                        if result != SortedStatus::Unknown {
                            return result;
                        };
                    }
                    json::JsonValue::Array(_) => {
                        let result = compare_lists(val1, val2);
                        if result != SortedStatus::Unknown {
                            return result;
                        };
                    }
                    _ => {
                        panic!("value is neither a list a number or a null")
                    }
                }
            }
            _ => {
                panic!("value is neither a list a number or a null")
            }
        }
    }
    SortedStatus::Unknown // if all values are equal, then this list does not affect the sortedness
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

