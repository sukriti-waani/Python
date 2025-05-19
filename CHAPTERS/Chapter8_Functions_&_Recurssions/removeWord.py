#  Python function to remove a given word from a list ad strip it at the same time.

def remove(l ,word):
  n = []  # Creates a new empty list `n` to store the results
  for item in l:
    if not(item == word):  #  Checks if the current item is NOT equal to `word`
      n.append(item.strip(word))  # If so, strip the characters in `word` from both ends of `item` and add to `n`
  return n

l = ["Suk", "Rohan" , "Raman", "an"]
print(remove(l, "an"))