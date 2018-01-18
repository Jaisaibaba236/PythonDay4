import random

fil = open("/home/jaisaibaba236/Desktop/words.txt")
word_dictionary = dict()
inverse = dict()

def search_key(fil):
  for i in fil:
    word_dictionary[i.strip()] = random.random()
  invert_dict(word_dictionary)

def invert_dict(word_dictionary):
    for keys in word_dictionary:
      val = word_dictionary[keys]
      inverse.setdefault(val,keys)   
    print (inverse)

search_key(fil)
