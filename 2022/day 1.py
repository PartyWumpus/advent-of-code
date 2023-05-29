data = open('data.txt','r')
list = data.read().split('\n\n')
highest = 0
for elf in list:
  value = 0
  for line in elf.split("\n"):
    value += int(line)
  if value > highest:
    highest = value
    print(highest)
