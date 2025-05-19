def goodDay(name, ending):
  print("Good day , " + name + "!")
  print(ending)
  return "done"

# goodDay("Waani" , "Thank you")
a = goodDay("Sourya" , "Thanks")
print(a)


#  Prevent a python print() function to print a new line at the end.
print("b")
print("c")
print("d", end="")
print("e", end="")