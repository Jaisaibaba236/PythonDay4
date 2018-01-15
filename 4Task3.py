
from functools import reduce

def evenlist():
 list1 = []
 for i in range(1,5):
   if i%2 == 0:
     list1.append(i)
 print(list1)    
 return list1
  
def square(x,y):
   return (x**2+y**2)**0.5

even = evenlist()
     
ans = reduce(square,even)
print(round(ans**2))
