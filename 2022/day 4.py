data = open('data.txt','r').read().split("\n")

# format = a-b
# example: 5-8 = 5678
def get_values_in_range(values):
  output = ""
  values = values.split('-')
  value1 = int(values[0])
  value2 = int(values[1])
  for i in range(value1, value2+1):
    output += str(i)
  return [value1, value2]
  #return output

num = 0
for pair in data:
  pair = pair.split(',')
  elf1, elf2 = pair[0], pair[1]
  elf1range = get_values_in_range(elf1)
  elf2range = get_values_in_range(elf2)
  #if (elf1range[0] >= elf2range[0] and elf1range[1] <= elf2range[1]) or (elf1range[0] <= elf2range[0] and elf1range[1] >= elf2range[1]):
  #  print(elf1, elf2)
  #  num += 1
  overlap = False
  for item in range(elf1range[0], elf1range[1]+1):
    if item in range(elf2range[0],elf2range[1]+1):
      overlap = True
  if overlap == True:
    print(elf1range,elf2range)
    num += 1
print(num)
