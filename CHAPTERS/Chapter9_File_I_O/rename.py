# Program to rename a file to "renamed_by_python.txt"

with open("rename.txt") as f:
  content = f.read()

with open("renamed_by_python.txt", "w") as f:
  f.write(content)