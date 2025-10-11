# 11
# from mypackage import m1, m2

# print("Addition:", m1.add(3, 5))
# print("Multiplication:", m2.multiply(4, 6))


# 12
# from mypackage import add, multiply

# print("Addition:", add(10, 20))
# print("Multiplication:", multiply(5, 3))


# 13 Importing from a Package
# import mypackage

# print("Addition:", mypackage.add(8, 2))
# print("Multiplication:", mypackage.multiply(3, 7))


# 14
# from mypackage import add, multiply

# print("Addition:", add(5, 10))
# print("Multiplication:", multiply(4, 9))


# 15 : Handling Package Import Errors
try:
    from mypackage import divide
except ImportError:
    print("Error: The function you are trying to import does not exist.")
