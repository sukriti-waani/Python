n = int(input("Enter the number: "))
prod = 1

for i in range(1, n+1):
  prod = prod * i

print(f"The factorial of {n} is {prod}")