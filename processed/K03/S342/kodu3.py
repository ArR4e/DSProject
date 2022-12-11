n = int(input("Sisestage, mitut naturaalarvu kasutada: "))
x1 = 1
x2 = 1
y1 = 0
y2 = 0
while x1 <= n:
    y1 += x1**2
    x1 += 1
while x2 <= n:
    y2 += x2
    x2 += 1
a = y2**2 - y1
print(a)