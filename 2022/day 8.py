data = open('data.txt','r').read().split("\n")
from copy import deepcopy

dirs = [[1,0],[-1,0],[0,1],[0,-1]]
def move(coord, delta):
  coord[0] += delta[0]
  coord[1] += delta[1]

def score(coord):
  value = data[coord[1]][coord[0]]
  score = 1
  for dir in dirs:
    checkCoord = deepcopy(coord)
    done = False
    dirscore = 0
    while not done:
      move(checkCoord,dir)
      if is_outside(checkCoord):
        break
      dirscore += 1
      if data[checkCoord[1]][checkCoord[0]] >= value:
        break
    score *= dirscore
  return score

def is_outside(coord):
  if coord[0] < 0 or coord[0] > len(data[0])-1 or coord[1] < 0 or coord[1] > len(data)-1:
    return True
  return False

highestScore = 0
for y in range(0,len(data)):
  for x in range(0,len(data[y])):
    points = score([x,y])
    if highestScore < points:
      highestScore = points
      print(x,y,data[y][x], highestScore)
