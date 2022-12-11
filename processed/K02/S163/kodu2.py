pikkus = int(input('Sisesta liini pikkus meetrites: '))
max_kaugus = int(input('Sisesta postide maksimaalkaugus meetrites: '))
summa = 0
x = 1

while summa < pikkus:
    x += 1
    summa += max_kaugus
    
print(x)
