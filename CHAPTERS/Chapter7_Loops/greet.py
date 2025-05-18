# Greet all the person names stored in list 'l' and which starts with S.

l = ["Suk", "Sohan", "Waani", "Shristi", "Sourya", "Umesh"]

for name in l:
  if(name.startswith("S")):
    print(f"Hello {name}")