fil = open("/home/jaisaibaba236/Desktop/words.txt")
temp_list = []
word_list = []

def has_duplicate(fil):
  for i in fil:
    word_list.append(i.strip())
  for value in word_list:
    temp_list.append(value)
    refined = word_list.pop(0)
    if value in word_list:
       return True
    return False

print(has_duplicate(fil))
