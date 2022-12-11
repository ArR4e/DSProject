n = input("Sisesta naturaalarv: ")
n = int(n)
summ = 0
summ1 = 0
a = n

if n < 0:
    print("Tegu pole naturaalarvuga")
    
while a > 0:
    summ += a
    a -= 1
summruut = summ**2

while n > 0:
    summ1 = summ1 + n**2
    n -= 1
     
print(summruut - summ1)
