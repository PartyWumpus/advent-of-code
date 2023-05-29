data = open('data.txt','r').read().split("\n")
duplicates = []

scores = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# combine every 3 lines into one
newdata = []
i = 0
while i < len(data):
  newdata.append( [data[i], data[i+1], data[i+2]] )
  i += 3


for line in newdata:
  halflength = len(line)//2
  #compartment1 = line[:halflength]
  #compartment2 = line[halflength:]
  compartment1 = line[0]
  compartment2 = line[1]
  compartment3 = line[2]
  duplicateItem = ""
  for item in compartment1:
    if item in compartment2 and item in compartment3:
      duplicateItem = item
  duplicates.append(duplicateItem)

score = 0
for item in duplicates:
  score += (scores.index(item)+1)
print(score)
