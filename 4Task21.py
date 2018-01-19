import operator
s = 'JAJAJAJVUVUUSSSSS'
n = ''
dictionary = dict()

def most_freq(s):
  global n
  for i in s:
     dictionary[i] = s.count(i)
     sort = s.replace(i,"")
     values = dictionary.values()
  print(dictionary)
   
  my_tuple = sorted(dictionary.items(), key=operator.itemgetter(1))[::-1]
  print(my_tuple)
  
  for x,y in my_tuple:
      n = n+(x*y)      
  return n

print(most_freq(s))

	
