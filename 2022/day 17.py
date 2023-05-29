data = open('testdata.txt','r').read()
rocksData = open('rocks.txt','r').read().split("\n\n")
from time import sleep

def parse_rocks(rocksTxt):
  rocks = []
  for rockTxt in rocksTxt:
    rock = []
    rockTxt = rockTxt.split('\n')[::-1]
    for y in range(len(rockTxt)):
      row = rockTxt[y]
      for x in range(len(row)):
        if row[x] == '#':
          rock.append((x,y))
    rocks.append(rock)
  return rocks

def parse_moves(movesTxt):
  moves = []
  for char in movesTxt:
    if char == '<':
      moves.append((-1,0))
    if char == '>':
      moves.append((1,0))
  return moves


def apply_delta(listOfCoords, delta):
  newList = []
  for coord in listOfCoords:
    newCoord = (
      coord[0] + delta[0],
      coord[1] + delta[1]
    )
    newList.append(newCoord)
  return newList

# sorry for code duplication :(
def find_lowest(points):
  lowy, lowx = float('-inf'), float('-inf')
  for point in points:
    if point[0] > lowx:
      lowx = point[0]
    if point[1] > lowy:
      lowy = point[1]
  return lowx, lowy

def find_highest(points):
  highy, highx = float('inf'), float('inf')
  for point in points:
    if point[0] < highx:
      highx = point[0]
    if point[1] < highy:
      highy = point[1]
  return highx, highy

def place_rock(rock):
  lowy = find_highest(rock)[1]
  return apply_delta(rock, (3,lowy+highestPoint+4))

def is_outside(rock):
  for coord in rock:
    if coord[0] <= 0 or coord[0] >= 8:
      return True
  return False

def is_grounded(rock):
  if find_lowest(rock)[1] <= 0: # 0 is floorPos
    return True
  for coord in rock:
    if coord in allRockCoords:
      return True
  return False

def visualise_data(rock):
  highest = find_lowest(rock)[1]
  for y in range(highest+1,highest-25,-1):
    row = "|"
    for x in range(1,8):
      if (x, y) in rock:
        row += "@"
      elif (x, y) in allRockCoords:
        row += "#"
      elif y == 0:
        print('+-------+')
        return
      else:
        row += "."
    print(row+"|")
  print()

'''
def find_pattern(allRockCoords):
  shape1 = allRockCoords[:len(allRockCoords)//2]
  shape2 = allRockCoords[len(allRockCoords)//2:]
  shape2 = apply_delta(shape2,(0,-find_highest(shape2)[1]))
  if set(shape1) == set(shape2):
    return True
  return False
'''

def find_new_floor(allRockCoords):
  y = find_lowest(allRockCoords)[1]
  for x in range(1,8):
    if not ((x, y) in allRockCoords):
      return False
  return True

def find_any_floor(allRockCoords):
  y = find_lowest(allRockCoords)[1]
  for y in range(0,y):
    found = True
    for x in range(1,8):
      if not ((x, y) in allRockCoords):
        found = False
    if found == True:
      return True

#listb = [(1,2),(2,2),(3,2),(4,2),(5,2),(6,2),(7,2),(7,1)]
#print(find_new_floor(listb))
#a = 5/0

highestPoint = 0
rockNum = -1
totalRockNum = 0
allRockCoords = []
moveNum = -1
rocks = parse_rocks(rocksData)
moves = parse_moves(data)
while totalRockNum < 202200:
  totalRockNum += 1
  rockNum = (rockNum + 1) % len(rocks)
  rock = place_rock(rocks[rockNum])

  finished = False
  while not finished:
    moveNum = (moveNum + 1) % len(moves)
    # move side to side
    newRock = apply_delta(rock, moves[moveNum])
    if not is_outside(newRock) and not is_grounded(newRock):
      rock = newRock

    # move down
    newRock = apply_delta(rock, (0,-1))
    if not is_grounded(newRock):
      rock = newRock
    else:
      highPoint = find_lowest(rock)[1]
      if highPoint > highestPoint:
        highestPoint = highPoint
      allRockCoords += rock
      finished = True
  if find_new_floor(allRockCoords):
    print("woaski", totalRockNum)
    visualise_data(rock)
  if totalRockNum % 200 == 0:
    print(totalRockNum)
