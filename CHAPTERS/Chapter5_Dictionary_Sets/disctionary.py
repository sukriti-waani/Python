#  Dictionary is a collection of key-value pairs.
#  Properties - It is unorderd, mutable, indexed, and cannot contain duplicate keys.

# marks = {
#   "Sukriti" : 90,
#   "Rohan" : 82,
#   "Sohan" : 25
# }

# # print(marks, type(marks))
# print(marks["Rohan"])


# Dictionary Methods
marks = {
  "Sukriti" : 90,
  "Rohan" : 82,
  "Sohan" : 25,
  0 : "Sukriti"
}

print(marks.items())  # It gives a key value pair
print(marks.keys())  # Gives keys of marks
print(marks.values())  # Gives values of marks
marks.update({"Sukriti" : 92, "Shyam" : 95})
print(marks)

print(marks.get("Rohan"))  # Prints none
print(marks["Rohan"])  # Returns an error
# When we use [] bracket then we get error if key does not exist in the dictionary and .get() gives none

