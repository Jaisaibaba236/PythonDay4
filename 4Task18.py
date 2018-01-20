fil = open("/home/jaisaibaba236/Desktop/words.txt")
word_list = []

def has_duplicate(fil):
  for i in fil:
     word_list.append(i.strip())
  for value in word_list:
     x = word_list.pop(0)
     if x in word_list:
        print(x)
        return True
  return False
     
print(has_duplicate(fil))
