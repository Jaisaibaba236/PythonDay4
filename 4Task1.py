list1 = [1,2,3,4]
list2 = [3,4,5,7,[2,3,12,23,34]]
list1.append(list2)

print(list1)

def nested_sum(list1):
 sum1=0
 sum2=0
 sum3=0
 for i in list1:
  if type(i) == int:
    sum1 += i
  else:
    for j in i:
     if type(j) == int:
       sum2 += j
     else:
       sum3 += sum(j)
 print(sum1+sum2+sum3)
 
nested_sum(list1)
