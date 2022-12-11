n = int(input("sisesta naturaalarvude kogus"))
a = 1
x = 0
i = 0
a2= 1
x2= 0
i2= 0
while i<n:
    x = x + a**2
    a = a + 1
    i = i + 1
    
while i2<n:
  x2= (x2+a2)
  a2= a2+1
  i2= i2+1
x2= (x2)**2
print(x2-x)
