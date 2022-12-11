import math
a = int(input("Sisesta liini pikkus täisarvuna meetrites: "))
b = int(input("Sisesta kõrvuti olevate postide maksimaalkaugus teineteisest täisarvuna meetrites: "))

c = a/b

if a == b:
    print(2)
else:
    print(math.ceil(c)+1)