natarv = int(input("Sisesta naturaalarv: "))
rsumma = 0
a = []
for x in range(natarv+1):
    rsumma = rsumma+ x**2
    a.append(x)
summar = sum(a)**2
print(summar - rsumma)
    
