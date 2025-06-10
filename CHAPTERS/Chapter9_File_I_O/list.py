# A file contains a word "Donkey" multiple times. We need to write a program which replace this word with #### by updating the same file.
# Repeat Donkey program for a list of such words to be censored.

words = ["Donkey", "good", "bad"]

with open("donkey.txt", "r") as f:
    content = f.read()

# Replace each word in the list
for word in words:
    content = content.replace(word, "#" * len(word))

# Write the updated content back to the file
with open("donkey.txt", "w") as f:
    f.write(content)
