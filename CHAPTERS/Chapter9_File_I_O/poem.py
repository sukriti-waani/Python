# Read the text from a given file 'poem.txt' and find out whether it contains word 'twinkle'

f = open("poem.txt")
f.read()
if("twinkle" in content):
  print("The word twinkle is present in the content")

else:
  print("The word twinkle is not present in the content")

f.close()