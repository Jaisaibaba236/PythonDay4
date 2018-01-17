def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)


x = int(input("Enter any value:"))
for i in range(x):
  print(fib(i))
