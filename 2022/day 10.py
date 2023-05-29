data = open('data.txt','r').read().split("\n")

registerValues = [1]

def noop():
  registerValues.append(registerValues[-1])

def addx(num):
  noop()
  registerValues.append(registerValues[-1]+num)

def sig_strength(index):
  return registerValues[index-1] * index

def find_positions(value):
  positions = []
  positions.append(value)
  positions.append(value-1)
  positions.append(value+1)
  return positions

for line in data:
  if line == 'noop':
    noop()
  else:
    addx(int(line[4:]))

#result = sig_strength(20) + sig_strength(60) + sig_strength(100) + sig_strength(140) + sig_strength(180) + sig_strength(220)
#print(result)

text = ""
for index in range(240):
  if index%40 in find_positions(registerValues[index]):
    text += '#'
  else:
    text += ' '

print(text[0:40])
print(text[40:80])
print(text[80:120])
print(text[120:160])
print(text[160:200])
print(text[200:240])
