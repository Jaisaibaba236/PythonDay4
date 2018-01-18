import random

fil = open("/home/jaisaibaba236/Desktop/words.txt")
word_dictionary = dict()

def search_word(fil):
  for i in fil:
    word_dictionary[i.strip()] = random.random()
  print(sorted(word_dictionary.keys()),sorted(word_dictionary.values()))
    
print(search_word(fil))
