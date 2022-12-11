n = int(input("Sisestage naturaalarv n: "))

arrruutsum = list(range(1, n+1))
arrsumruut = range(1, n+1)

for i in range(len(arrruutsum)):
    arrruutsum[i] = arrruutsum[i]**2
    
ruutsum = sum(arrruutsum)

sumruut = sum(arrsumruut)**2

print(abs(sumruut-ruutsum))