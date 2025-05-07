a = int(input("Enetr your age: ")) 

# If elif else ladder
# If else and Elif statemnts are a multiway decision taken by our program due to certain conditions in our code.

if(a >= 18):
  print("You are above the age of concent")

elif(a < 0):
  print("You are entering an invalid age")

elif(a == 0):
  print("You are entering 0 which is not a valid age")

else:
  print("You are below the age of concent")

print("End of program")

# NOTE
# 1.  There can be any number of Elif statements.
# 2.  Last else is executed only if all the conditions inside Elifs fail.