import math

pikkus = int(input("Liinipikkus: "))
maxKaugus = int(input("Maksimaalne kaugus: "))

i = 1
while True:
    if pikkus/i > maxKaugus:
        i+=1
        continue
    else:
        print(i + 1)
        
        break