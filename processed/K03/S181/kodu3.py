arv = int(input("Sisestage naturaalarv: "))
a = 0
for x in range(arv):
    a = a + (x+1)**2
b = 0
for x in range(arv+1):
    b += x
c = b**2
print(c-a)
    