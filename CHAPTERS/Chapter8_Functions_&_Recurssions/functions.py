# Function is a group of statements performing a specific task.

#  Function Definition : The part containing the exact set of instructions which are executed when the function is called. 
def avg():
  a = int(input("Enter your first number: "))
  b = int(input("Enter your second number: "))
  c = int(input("Enter your third number: "))

  average = (a + b + c) / 3
  print(average)

#  Function Call : Whenever we want to call a function, we put the name of the function followed by the parameters enclosed in parentheses.
avg()     


#  Types of Functions : 
#     Built in functions (Already present in python) :      print(), len(), max(), min(), range()
#     User defined functions (Defined by the user)
