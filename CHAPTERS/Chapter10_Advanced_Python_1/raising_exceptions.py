a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b == 0):
  raise ZeroDivisionError("Hey our program is not meant to divide by zero")

else:
  print(f"The divison a/b is {a/b}")