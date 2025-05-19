#  Using functions, find greatest of three numbers

def greatest(a, b, c):
  if(a > b and a > c):
    return a
  elif(b > a and b > c):
    return b
  elif(c > a and c > b):
    return c
  
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

ans = greatest(a, b, c)
print(ans)