# Program to find out the line number where python is present


with open("log.txt") as f:
  lines = f.readlines()

lineno = 1
for line in lines:
  if("Python" in line):
    print(f"Yes python is present. Line no: {lineno}")
    break
  lineno += 1

else:
  print("No Python is present")