list1 = list(range(1,16))

def multiple(n):
 finallist = [] 
 for i in list1:
   if n%5 == 0:
    finallist.append(i)
 return finallist
 
print(list(filter(multiple,list1)))
