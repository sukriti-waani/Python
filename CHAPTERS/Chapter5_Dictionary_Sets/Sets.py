# SETS is a collection of non-reptitive elements

d ={} # Empty dictionary

e = set() # Empty set and dont't use s = {} as it will create an empty dictionary

s2 = {1, 5, 30}
print(s2)
s1 = {1, 32, 5, 5, 5, 55, 5}
print(s1)
s = {1, 32, 5, 5, 5, 55, 5, "Sukriti"}
print(s, type(s))


# SET  METHODS
s.add(95)
print(s, type(s))

# use chatgpt to know more about set methods

#Properties of sets
#1. Unordered collection of unique elements
#2. Unindexed
#3. No duplicate elements
#4. No indexing
#5. No slicing
#6. No insertion or deletion of elements by index
#7. There is no way to change items in sets.


#SET OPERATIONS
len(s)
s.remove(95)
s.pop() # removes random element from the set and return the elements removed.
s.clear() #empties the set
s.union({4,15}) #Returns a new set with all items from both sets.
s.intersection({4,15}) #Returns a new set with elements common to both sets.

s3 = {1, 23, 6}
s4 = {7, 18, 1, 6}
print(s3.union(s4))
print(s3.intersection(s4))

