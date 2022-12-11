naturaalarv = int(input("Sisesta naturaalarv: "))
n = 0
x = 0
while naturaalarv >= n:
    x = x + n**2
    n = n + 1

n = 0
y = 0
while naturaalarv >= n:
    y = (y + n)
    n = n + 1

y = y**2

z = y - x
print(z)