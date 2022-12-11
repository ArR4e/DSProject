import math
liinipikkus = int(input("Palun sisesta, kui pikk peab liin olema: "))
maxpikkus = int(input("Palun sisesta, mis on maksimaalne pikkus kahe posti vahel: "))
minpostidearv = (math.ceil(liinipikkus/maxpikkus))+1
print(minpostidearv)