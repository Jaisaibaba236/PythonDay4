diction=dict()
fin = open("Words.txt")

def dictionary(string):
  for char in fin:
    diction[char] += 1
    if string in diction:
     return True
    else:
     return False
  
print(dictionary("Gyan"))
