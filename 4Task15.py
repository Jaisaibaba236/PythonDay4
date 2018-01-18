import random

fil = open("/home/jaisaibaba236/Desktop/words.txt")
word_dictionary = dict()
matching_keys = []

keylist = ['aa','a','receives','janglers']

def search_key(fil,keylist):
  for i in fil:
    word_dictionary[i.strip()] = random.random()
  for keys in word_dictionary:
    if keys in keylist:
      matching_keys.append(keys)
    else:
      continue
  return matching_keys

print(search_key(fil,keylist))
