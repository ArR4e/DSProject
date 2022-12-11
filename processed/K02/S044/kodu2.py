x = int(input("Sisesta kogupikkus"))
y = int(input("Sisesta postide maksimaal vahe"))
z = 2
d = x / y
p = y
if d > 1:
    while p <= x:
        p += y
        z += 1
else:
    pass
if x == 2:
    print("3")
else:
    print(z)


