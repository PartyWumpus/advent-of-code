data = open('data.txt','r').read().split("\n")

class Stack():
  def __init__(self):
    self.data = []

  def peek(self):
    return self.data[-1]

  def add_item(self, item):
    self.data.append(item)

  def move_item(self, stack2):
    stack2.data.append(self.data.pop(-1))

  def move_items(self, stack2, num):
    moved = []
    for i in range(num):
      moved.append(self.data.pop(-1))
    moved = moved[::-1]
    stack2.data += moved

class Stacks():
  def __init__(self, numStacks):
    self.data = []
    for i in range(numStacks):
      self.data.append(Stack())

  def set(self, index, value):
    self.data[index-1].add_item(value)

  def print_data(self):
    for i in range(len(self.data)):
      print(i+1, self.data[i].data)

  def move_item(self, index1, index2):
    self.data[index1-1].move_item(self.data[index2-1])

  def move_items(self, index1, index2, num):
    self.data[index1-1].move_items(self.data[index2-1], num)


# data[0:8] = stacks
# data[8] = index names
# data[10:] = moves

# make stacks
stacks = Stacks(int(data[8][-2]))
for line in data[7::-1]:
  # format = [S] [W]         [F]     [W] [V]
  for i in range(1,10,1):
    if line[i*4 - 3] != " ":
      stacks.set(i, line[i*4 - 3])

# go through the motions
stacks.print_data()
print()
for line in data[10:]:
  num = int(line[ line.index("move")+5 : line.index("move")+7 ])
  startPos = int(line[ line.index("from")+5])
  endPos = int(line[ line.index("to")+3])
  #for i in range(num):
  #  stacks.move_item(startPos, endPos)
  stacks.move_items(startPos, endPos, num)
stacks.print_data()

