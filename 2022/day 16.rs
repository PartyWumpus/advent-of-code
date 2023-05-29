use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::cmp;

fn main() {
    let mut valves: HashMap<String, (i32, Vec<String>)> = HashMap::new();

    if let Ok(lines) = read_lines("./testdata.txt") {
        for line in lines {
            if let Ok(data) = line {
                let name = &data[6..8];
                let name = name.to_string();
                let flow_rate =  &data[23.. data.find(";").unwrap()].parse::<i32>().unwrap();

                let mut list: Vec<String> = Vec::new();
                for x in data[data.find(";").unwrap()+24..].split(", ") {
                    list.push(x.trim().to_string());
                }
                valves.insert(name, (*flow_rate, list));
            }
        }
    }
    println!("{:#?}", valves);

    let active_valves: Vec<String> = Vec::new();
    println!("{:?}", goto_valve("AA", &valves, active_valves, 0, 0));
}

fn goto_valve(valve: &str, valves: &HashMap<String, (i32, Vec<String>)>, active_valves: Vec<String>, minute: i32, total: i32) -> i32 {
  if minute == 30 {return total}

  let mut total = total;
  // add valves
  for active_valve in &active_valves {
    total += valves[active_valve].0;
  }

  if !active_valves.contains(&valve.to_string()) { // try turning on valve
    let mut new_active_valves = active_valves.clone();
    new_active_valves.push(valve.to_string());
    total = cmp::max(goto_valve(valve, valves, new_active_valves, minute+1, total), total);
  }
  for new_valve in &valves[valve].1 {
    total = cmp::max(goto_valve(new_valve, valves, active_valves.clone(), minute+1, total), total);
  }
  return total
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

