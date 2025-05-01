#  Lists are container to store a set of values of any data types

a = ["Apple", "Orange" , 5, 34.68, False, "Hello"]
print(a)

# a[0] = "Grapes" # Unlike strings lists are mutable
# print(a[0])
# print(a[1:4])

a.append("Sukriti")
print(a)

l1 = [1, 34, 45, 0 , 23]

# l1.sort()
# print(l1)

# l1.reverse()
# print(l1)

l1.insert(3, 1000)
print(l1)

l1.pop(2)
print(l1)
print(l1.pop(2))
