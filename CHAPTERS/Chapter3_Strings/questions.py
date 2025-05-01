# User entered strings
# name = input("Enter your name \n")
# print(f"Good evening {name}")


# Chaining of replace
letter = '''Dear <|Name|>,
You are selected
<|Date|>'''
print(letter.replace("<|Name|>", "Sukriti").replace("<|Date|>", "30 April 2025"))


# Detect double space
name = "Sukriti is a good  girl"
print(name.find("  "))


# Replace double space with single spaces
name = "Sukriti is a good  girl"
print(name.replace("  ", " "))
print(name) # Strings are immutable which means that we cannot change them by running functions on them


# Format the letter using escape sequence characters
letter1 = "Dear Sukriti, \n\tYou are learning Python. \nThanks!"
print(letter1)