data = open('testdata.txt','r').read().split("\n")
from copy import deepcopy

mostGeodesEachMin = [0]*24
def find_moves(oldGameState, upcomingRobot=None):
  global i
  global blueprint, highestScore
  gameState = deepcopy(oldGameState)
  gameState['movesMade'].append(upcomingRobot)
  if gameState['minute'] == 24:
    if gameState['items']['geode'] > highestScore:
      highestScore = gameState['items']['geode']
      print(highestScore, gameState['movesMade'])
    return

  i += 1
  if i % 50000 == 0 :
    print(i, mostGeodesEachMin)

  for robot in gameState['robots']:
    gameState['items'][robot] += gameState['robots'][robot]

  if gameState['items']['geode'] < mostGeodesEachMin[gameState['minute']]:
    return

  if gameState['items']['geode'] > mostGeodesEachMin[gameState['minute']]:
    mostGeodesEachMin[gameState['minute']] = gameState['items']['geode']

  if upcomingRobot != None:
    gameState['robots'][upcomingRobot] += 1
    if upcomingRobot == 'ore':
      gameState['items']['ore'] -= blueprint['ore']
    elif upcomingRobot == 'clay':
      gameState['items']['ore'] -= blueprint['clay']
    elif upcomingRobot == 'obsidian':
      gameState['items']['ore'] -= blueprint['obsidianOre']
      gameState['items']['clay'] -= blueprint['obsidianClay']
    else:
      gameState['items']['ore'] -= blueprint['geodeOre']
      gameState['items']['obsidian'] -= blueprint['geodeObsidian']


  gameState['minute'] += 1

  if blueprint['geodeOre'] <= gameState['items']['ore'] and blueprint['geodeObsidian'] <= gameState['items']['obsidian']:
    find_moves(gameState,'geode')
  elif blueprint['obsidianOre'] <= gameState['items']['ore'] and blueprint['obsidianClay'] <= gameState['items']['clay']:
    find_moves(gameState,'obsidian')
  else:
    moves = []
    if blueprint['ore'] <= gameState['items']['ore']:
      moves.append(0, 'ore')
    if blueprint['clay'] <= gameState['items']['ore']:
      moves.append(0, 'clay')
    for move in moves:
      find_moves(gameState,move)


i = 0
for line in data:
  highestScore = -1
  bInfo = line[line.find(':')+1:].split('.')[:-1]
  blueprint = {
    'num': int(line[10:(line.find(':'))]),
    'ore': int(bInfo[0][22:bInfo[0].rfind('ore')]),
    'clay': int(bInfo[1][23:bInfo[1].rfind('ore')]),
    'obsidianOre': int(bInfo[2][27:bInfo[2].rfind('ore')]),
    'obsidianClay': int(bInfo[2][37:bInfo[2].rfind('clay')]),
    'geodeOre': int(bInfo[3][24:bInfo[3].rfind('ore')]),
    'geodeObsidian': int(bInfo[3][34:bInfo[3].find('obsidian')])
  }
  gameState = {
    'items':{'ore':0,'clay':0,'obsidian':0,'geode':0},
    'robots':{'ore':1,'clay':0,'obsidian':0,'geode':0},
    'minute':1,
    'movesMade':[]
  }
  find_moves(gameState)
  print(highestScore)
