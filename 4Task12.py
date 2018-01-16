fin = open("Words.txt")
diction=dict()

def dictionary(string):
  for char in fin:
    diction[char] = 1
    if string in diction:
     return True
    else:
     x = False
  return x

print(dictionary("Gyan"))

List Lookup:
  
fin = ['abc','bcd','cde','def','efg']
diction=dict()

def dictionary(string):
  j=0
  for i in fin:
    j=j+1
    diction[j] = i
    val = diction.values()
    if string in val:
     return True
    else:
     x = False
  return x
  print(diction)
print(dictionary('2131'))
