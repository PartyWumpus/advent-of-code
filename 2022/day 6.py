data = open('data.txt','r').read()

found = False
packetLength = 14
i = packetLength-1
while not found:
  i += 1
  chars = data[i-packetLength:i] # most recent 'packetLength' number of chars
  if len(set(chars)) == packetLength:
    found = True
print(chars, i)
