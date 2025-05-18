# break statement
for i in range(50):
  if(i == 25):
    break # Exit the loop right now
  print(i)


# continue statement
for i in range(50):
  if(i == 25):
    continue # Skip the iteration
  print(i)


# pass statement
for i in range(50):
  pass # Null statemnt in Python instructs to Do nothing

i = 0
while(i < 45):
  print(i)
  i += 1