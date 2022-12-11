n = int(input("anna n "))
x = 1
y = 0
z = 0

while n != 0:
    y += x * x
    z += x
    x += 1
    n -= 1
    
z = z * z
print("summa erinevus on " + str(z - y))