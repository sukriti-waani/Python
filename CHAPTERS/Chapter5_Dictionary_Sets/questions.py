# Create a dictionary of Hindi words with values as their English translations.

# hindi_words = {
#   "madad": "Help",
#   "kursi": "Chair",
#   "billi" : "Cat",
# }

# word = input("Enter the word you want to translate: ")
# print(hindi_words[word])


# Input five numbers from the user and display all the unique numbers(once).
# s = set()
# n = input("Enter number 1: ")
# s.add(int(n))
# n = input("Enter number 2: ")
# s.add(int(n))
# n = input("Enter number 3: ")
# s.add(int(n))
# n = input("Enter number 4: ")
# s.add(int(n))
# n = input("Enter number 5: ")
# s.add(int(n))

# print(s)


# Can we have a set with 18 (int) and '18' (str) as a value in it ?
# s= set()
# s.add(18)
# s.add("18")
# print(s)  # YES !!


# Length of s
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s) 
# Comparison operator check the value  and if both the values are same then type doesn't matter to python
# print(len(s))


# s = {}  # What is the type of 's' ?
# print(type(s))  # Output: <class, 'dict'>
# s = {}  # dictionary



# Create an empy dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
# d = {}

# name = input("Enter friends name: ")
# lang  = input("Enetr language name: ")
# d.update({name: lang})

# name = input("Enter friends name: ")
# lang  = input("Enetr language name: ")
# d.update({name: lang})

# name = input("Enter friends name: ")
# lang  = input("Enetr language name: ")
# d.update({name: lang})

# name = input("Enter friends name: ")
# lang  = input("Enetr language name: ")
# d.update({name: lang})

# print(d)

# If the names of two friends are same; then update method will keep updating the value


# Can we change the values inside a list which is conatined in set S ?
# s = {8, 7, 12, "Sukriti", [1,2]}
# s[4][0] = 9
# No, we can't change the values inside a list which is contained in set S. In fact, we cannot even access the list inside the set S. The values can be same.
# Sets in Python require all their elements to be immutable and hashable. 
# Lists are mutable and hashable, so they cannot be added to a set.