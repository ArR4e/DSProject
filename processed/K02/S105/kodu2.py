x = int(input("Sisesta liini pikkus: "))
y = int(input("Sisesta maksimaalne postidevaheline kaugus: "))
z = int(x % y)

if x<y:
    print("2")
elif z>0:
    print(str(x//y+2))
else:
    print(str(x/y+1))
