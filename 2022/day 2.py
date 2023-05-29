data = open('data.txt','r')
text = data.read().split('\n')

# enemy moves:
# A = Rock, B = Paper, C = Scissors

# my moves:
# X = Rock, Y = Paper, Z = Scissors

scores = {"X":1,"Y":2,"Z":3}
loseConditions = ['A Z','B X','C Y']
winConditions = ['A Y','B Z','C X']
drawConditions = ['A X','B Y','C Z']

score = 0
for round in text:
  choice = round[2]
  opponent = round[0]

  # X = lose, Y = draw, Z = win
  if choice == "Y":
    # if draw, my move = their move
    if opponent == 'A':
      round = 'A X'
    if opponent == 'B':
      round = 'B Y'
    if opponent == 'C':
      round = 'C Z'
  if choice == "X":
    # if lose, my move = losing move
    if opponent == 'A':
      round = 'A Z'
    if opponent == 'B':
      round = 'B X'
    if opponent == 'C':
      round = 'C Y'

  if choice == "Z":
    # if win, my move = winning move
    if opponent == 'A':
      round = 'A Y'
    if opponent == 'B':
      round = 'B Z'
    if opponent == 'C':
      round = 'C X'

  # scoring code
  score += scores[round[2]]
  if round in winConditions:
    score += 6
  if round in drawConditions:
    score += 3
  if round in loseConditions:
    score += 0
print(score)
