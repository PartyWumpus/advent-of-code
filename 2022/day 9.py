data = open('testdata2.txt','r').read().split("\n")
import time

def move(coord, delta):
  coord[0] += delta[0]
  coord[1] += delta[1]

def adjacent(coord1, coord2):
  if abs(coord1[1] - coord2[1]) <= 1 and abs(coord1[0] - coord2[0]) <= 1:
    return True
  return False

def find_move_vector(coord1, coord2):
  return normalize_vector([coord1[0]-coord2[0],coord1[1]-coord2[1]])

def normalize_vector(vector): # i don't think this is normalization but i'm not actually sure...
  # can't think of fun mathsy way to do this :(
  if vector[0] > 0:
    vector[0] = 1
  if vector[0] < 0:
    vector[0] = -1
  if vector[1] > 0:
    vector[1] = 1
  if vector[1] < 0:
    vector[1] = -1
  return vector

def display_state():
  headPos = positions[0]
  for y in range(headPos[1]+5,headPos[1]-5,-1):
    row = ''
    for x in range(headPos[0]-5,headPos[0]+5):
      if [x,y] == headPos:
        row += "H"
      elif [x,y] in positions:
        row += str(positions.index([x,y]))
      elif (x,y) in visited:
        row += "#"
      else:
        row += " "
    print(row)
  print()

def move_knot(pos, parentPos):
  if not adjacent(pos, parentPos):
      move(pos, find_move_vector(parentPos, pos))

dirs = {'R':[1,0],'L':[-1,0],'U':[0,1],'D':[0,-1]}

# positions[0] = the head
positions = []
for i in range(10):
  positions.append([0,0])
visited = set()

for line in data:
  display_state()
  dir = dirs[line[0]]
  amount = int(line[2:])
  for z in range(amount):
    move(positions[0], dir)
    for i in range(1,len(positions)):
      move_knot(positions[i],positions[i-1])
    visited.add(tuple(positions[-1]))
  print(line)
print(len(visited))
