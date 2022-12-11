import math
a = int(input("Sisesta elektriliini pikkus meetrites: "))
b = int(input("Sisesta elektriliini postide vaheline kaugus: "))

if a > b:
    print(math.ceil(a / b + 1))
elif a < b:
    print(2)
elif a == b:
    print(2)
