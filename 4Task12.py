import random
fil = open("/home/jaisaibaba236/Desktop/words.txt")
word_dictionary = dict()

def search_word(fil,search_value):
  for i in fil:
    word_dictionary[i.strip()] = random.random()  
  if search_value in word_dictionary:
    return True
  return False

print(search_word(fil,'receives'))
