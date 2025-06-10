# A file contains a word "Donkey" multiple times. We need to write a program which replace this word with #### by updating the same file.

word = "Donkey"

with open("donkey.txt", "r") as f:
  content = f.read()

contentNew = content.replace(word, "######")

with open("donkey.txt", "w") as f:
  f.write(contentNew)
