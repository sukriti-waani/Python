n = int(input("Enter the number: "))

for i in range(1, n+1):
  print(" " * (n-i), end = "")  #  n - i spaces are printed to shift the stars to the center.   end = "" ensures the next print() stays on the same line
  print("*" * (2*i - 1), end = "")  #  2*i - 1 ensures the star count is odd
  print("")   #  Moves to the next line after printing spaces and stars.

