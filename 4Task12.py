diction=dict()
fin = open("Words.txt")

def dictionary(string):
  for char in fin:
    diction[char]=fin
    if string in diction:
     return True
    else:
     return False
print(diction)
   
print(dictionary("Gyan"))
