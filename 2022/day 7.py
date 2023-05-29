data = open('data.txt','r').read().split("\n")

def cd(input):
  global location
  if input == "..":
    folder = str(location)
    location.pop(-1)
    # if leaving the file, it can have totalsize calculated
    # totalsize = size of direct children + size of contained folders
    # all contained folders will have already have their totalsize calculated, so no recursion necessary
    folders[folder]['totalsize'] += folders[folder]['size']
    for childFolder in folders[folder]['folders']:
      folders[folder]['totalsize'] += folders[childFolder]['totalsize']

    return
  if input == "/":
    location = ["/"]
    return
  location.append(input)

def ls():
  global folders
  # instanciate this folder in 'folders'
  folders[str(location)] = {'totalsize':0,'size':0,'folders':[]}
  i = lineNum
  while True:
    i += 1
    # if line doesn't exist or is a command, end
    if i >= len(data) or data[i][0] == "$":
      return

    file = data[i]
    if file[:3] == "dir":
      folderPath = str(location + [file[4:]])
      folders[str(location)]['folders'].append(folderPath)
    else:
      filesize = int(file.split(" ")[0])
      folders[str(location)]['size'] += filesize

# uses assumption that folder names are only used once
# not anymore it doesn't AS THAT IS WRONG!!! :(
# pretty simple change, dirs are now referred to as their whole path (as they should be anyways)
folders = {}

location = ["/"]
lineNum = -1
while lineNum < len(data)-1:
  lineNum += 1
  line = data[lineNum]

  # if command
  if line[0] == "$":
    if line[2:] == "ls":
      ls()
    else: #otherwise, command must be cd
      cd(line[5:])

# navigate back to / so all folders have totalsize set correctly
while location != []:
  cd('..')

# part 1
num = 0
for key in folders:
  folder = folders[key]
  if folder['totalsize'] <= 100000:
    num += folder['totalsize']
print(num)


# part 2
diskSpace = 70000000
freeSpaceGoal = 30000000
unusedSpace = diskSpace - folders["['/']"]['totalsize']
folderGoal = freeSpaceGoal - unusedSpace

lowestSuitableSize = diskSpace
for key in folders:
  size = folders[key]['totalsize']
  if size >= folderGoal and size < lowestSuitableSize:
    lowestSuitableSize = size
print(lowestSuitableSize)
