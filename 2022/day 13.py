data = open('testdata.txt','r').read().split("\n\n")

def compare_lists(left, right):
  # input lists = "[x,y,z]"
  left, right = left[1:-1], right[1:-1]
  # now "x,y,z"

  if len(right) < len(right):
    return False
  done = False
  i = 0
  while not done:
    if isList(left[i]) or isList(right[i]):
      if not isList(left[i]): print([left[i]], get_list(right, i))
      elif not isList(right[i]): print(get_list(left, i), [right[i]])
      else: print(get_list(left, i), get_list(right, i))
    else:
      print("NOT LIST", left[i], right[i])
      i += 2
    if i > len(left):
      return True

# input data
def get_list(str, index):
  i = str[index:].find("]") + index
  return str[i:index]


def isList(string):
  return (string[0] == "[")

for lines in data:
  left, right = lines.split('\n')
  compare_lists(left, right)

