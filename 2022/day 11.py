data = open('data.txt','r').read().split("\n\n")

def monkey_math(num, operation):
  if operation == 'old * old':
    return (int(num)*int(num)) % divisor# // 3
  if operation[4] == "*":
    return (int(num)*int(operation[6:])) % divisor# // 3
  if operation[4] == "+":
    return (int(num)+int(operation[6:])) % divisor# // 3

monkeys = {}
divisor = 1

# make monkeys
for monkey in data:
  monkey = monkey.split("\n")
  monkeyNum = monkey[0][7:-1]
  monkeys[int(monkeyNum)] = {
    'items':monkey[1][18:].split(','),
    'operation':monkey[2][19:],
    'test':int(monkey[3][21:]), # is divisible by
    'true':int(monkey[4][29:]),
    'false':int(monkey[5][30:]),
    'noInspected':0
  }
  # divisior to reduce size
  divisor *= monkeys[int(monkeyNum)]['test']

for round in range(10000):
  for monkeyNum in monkeys:
    # deal with each item
    for itemNum in range(len(monkeys[monkeyNum]['items'])):
      monkeys[monkeyNum]['items'][0] = monkey_math(monkeys[monkeyNum]['items'][0], monkeys[monkeyNum]['operation'])
      if monkeys[monkeyNum]['items'][0] % monkeys[monkeyNum]['test'] == 0:
        monkeys[monkeys[monkeyNum]['true']]['items'].append(monkeys[monkeyNum]['items'][0])
      else:
        monkeys[monkeys[monkeyNum]['false']]['items'].append(monkeys[monkeyNum]['items'][0])
      monkeys[monkeyNum]['items'].remove(monkeys[monkeyNum]['items'][0])
      monkeys[monkeyNum]['noInspected'] += 1

  if (round+1) % 1000 == 0:
    print(f"round: {round+1}")
    for monkey in monkeys:
      print(monkeys[monkey]['noInspected'])
    #for monkey in monkeys:
    #  print(monkeys[monkey]['items'])
    print()
