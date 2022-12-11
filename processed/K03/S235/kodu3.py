n = int(input("Sisestage naturaalarv: "))

i = 1
a = 0

while i <= n:
    a += i
    i = i + 1
    
b=0
while n>0:
    b= b+(n*n)
    n=n-1
    
print(a**2-b)
