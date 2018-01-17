list1 = [1,1,1,[1,1,1,[1,1,1,1,1],[1,1,1,1]]]

def nested_sum(list1):
 sum1=0
 for i in list1:
  if type(i) == int:
    sum1 += i
  else:
    sum1 += nested_sum(i)

 return(sum1)
 
print(nested_sum(list1))
