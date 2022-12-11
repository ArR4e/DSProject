import math

a = int(input("Liini pikkus: "))
b = int(input("Postide maksimaalkaugus: "))

print(int(math.ceil((a/b)+1)))