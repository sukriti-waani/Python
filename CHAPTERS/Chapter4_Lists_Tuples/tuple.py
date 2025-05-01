#  A tuple is an immutable data type in python

# a = (1,2,5,6)
# print(type(a))

# b = (22, ) # single element tuple
# print(type(b)) 

c = (1, 32, 589, True, "Hello", "Hey", 32)
print(c)

no = c.count(32)
print(no)

i = c.index("Hello")
print(i)

print(len(c))