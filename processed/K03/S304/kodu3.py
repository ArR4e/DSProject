n = int(input("sisesta naturaalarv: "))

a = 0
b = 0
for i in range(n):
     a += (i + 1)**2
     b += i + 1
c = b**2 - a

print(f"vastav väärtus on {c}.")
