def f_to_c(f):
  return 5 * (f - 32) / 9

far = int(input("Enter the temperature in Fahrenheit: "))
# print(f_to_c(far))
c = f_to_c(far)
print(f"{round(c, 2)} °C")


