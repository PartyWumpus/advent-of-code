data = open('data.txt','r').read().split("\n")
from copy import deepcopy
from random import shuffle

def add_vectors(pos1, pos2):
  pos3 = [
    pos1[0] + pos2[0],
    pos1[1] + pos2[1]
  ]
  return pos3

directions = [[-1,0],[1,0],[0,-1],[0,1]]
def check_pos(pos, distance):
  letter = data[pos[1]][pos[0]]
  if letter == "S": letter = "a"
  if letter == "E": letter = "z"
  for dir in directions:
    pos2 = add_vectors(pos,dir)
    try:
      if pos2[0] >= 0 and pos2[1] >= 0: # if value is within border
        letter2 = data[pos2[1]][pos2[0]]
        if letter2 == "E": letter2 = "z"
        if ord(letter) + 1 >= ord(letter2): # if letter is a valid square
          if visited[pos2[1]][pos2[0]] == '':
            visited[pos2[1]][pos2[0]] = distance
            sqrsToVisit[distance].append(pos2)
    except:
      pass

# find start positions
startPos = [0,0]
for index in range(len(data)):
  if data[index].find('S') != -1:
    startPos[1] = index
startPos[0] = data[startPos[1]].find('S')

endPos = [0,0]
for index in range(len(data)):
  if data[index].find('E') != -1:
    endPos[1] = index
endPos[0] = data[endPos[1]].find('E')

mapcopy = deepcopy(data)
#listOfStartPos = [[0,4],[0,0]]
listOfStartPos = [startPos]
while True:
  startPos = [0,0]
  for index in range(len(mapcopy)):
    if mapcopy[index].find('a') != -1:
      startPos[1] = index
  startPos[0] = mapcopy[startPos[1]].find('a')
  if startPos == [-1, 0]:
    break
  ugh = list(mapcopy[startPos[1]])
  ugh[startPos[0]] = 'A'
  mapcopy[startPos[1]] = ''.join(ugh)
  listOfStartPos.append(startPos)

shuffle(listOfStartPos) # should be faster?

# do search
lowestScore = 5000
amongus = 0
for startPos in listOfStartPos:
  amongus += 1
  visited = []
  for i in range(len(data)):
    visited.append(['']*len(data[0]))

  visited[startPos[1]][startPos[0]] = 0
  sqrsToVisit = {0:[startPos]}

  distance = 0
  while True:
    distance += 1
    sqrsToVisit[distance] = []
    for pos in sqrsToVisit[distance-1]:
      check_pos(pos, distance)
    if distance > lowestScore: # end early if not worth
      break
    if visited[endPos[1]][endPos[0]] != "":
      if int(lowestScore) > distance:
        lowestScore = distance
        print(lowestScore)
      break
  if distance == 508:
    for i in visited: print(i)
  if amongus % 50 == 0:
    print(f"# {amongus}")
print(lowestScore)
