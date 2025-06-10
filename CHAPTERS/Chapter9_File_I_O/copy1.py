# Program to make a copy of a text file "copy.txt" 

with open("copy.txt") as f:
  content = f.read()

with open("copy1.txt", "w") as f:
  f.write(content)