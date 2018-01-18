import random

fil = open("/home/jaisaibaba236/Desktop/words.txt")
word_dictionary = dict()

def search_word(fil,key):
  for i in fil:
    word_dictionary[i.strip()] = random.random()
  return word_dictionary.get(key,'Key not found!')
    
print(search_word(fil,'ab'))
