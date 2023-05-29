data = open('data.txt','r').read().split("\n")
from time import sleep

# input = list of [x, y]s
# output = list of all [x, y]s between those values as if they were a line
def line_coords(coords):
  points = set()
  for index in range(len(coords)-1):
    c1, c2 = coords[index], coords[index+1]
    if c1[0] != c2[0]:
      if c1[0] > c2[0]:
        for point in range(c2[0], c1[0]+1):
          points.add((point, c1[1]))
      else:
        for point in range(c1[0], c2[0]+1):
          points.add((point, c1[1]))

    else:
      if c1[1] > c2[1]:
        for point in range(c2[1], c1[1]+1):
          points.add((c1[0], point))
      else:
        for point in range(c1[1], c2[1]+1):
          points.add((c1[0], point))
  return points

def sand_fall(coord):
  global done
  if coord[1]+1 == floorPos:
    return coord
  if not ((coord[0], coord[1]+1) in allPoints):
    return sand_fall((coord[0], coord[1]+1))
  if not (coord[0]-1, coord[1]+1) in allPoints:
    return sand_fall((coord[0]-1, coord[1]+1))
  if not (coord[0]+1, coord[1]+1) in allPoints:
    return sand_fall((coord[0]+1, coord[1]+1))
  if coord == (500, 0):
    done = True
    return coord
  return coord # base case

def visualise_data(sandPos):
  for y in range(sandPos[1]-5,sandPos[1]+5):
    line = ""
    for x in range(sandPos[0]-5,sandPos[0]+5):
      if (x,y) in wallPoints:
        line += "#"
      elif (x,y) in sandPoints:
        line += "o"
      elif (x,y) == sandPos:
        line += "O"
      else:
        line += "."
    print(line)

def find_lowest(points):
  lowy, lowx = 0, 0
  for point in points:
    if point[0] > lowx:
      lowx = point[0]
    if point[1] > lowy:
      lowy = point[1]
  return lowx, lowy

# make walls
wallPoints = set()
for l in data:
  coords = []
  for segment in l.split(' -> '):
    coords.append( tuple(map(int,segment.split(","))))
  wallPoints = wallPoints.union(line_coords(coords))

floorPos = find_lowest(wallPoints)[1]+2

numSand = 0
sandPoints = set()
done = False
while not done:
  allPoints = sandPoints.union(wallPoints)
  coord = sand_fall((500, 0))
  if numSand % 100 == 0:
    print(numSand)
  sandPoints.add(coord)
  numSand += 1
print(numSand)
