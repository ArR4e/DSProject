import math

liinTotal = int(input("Liini pikkus (m): "))
liinGap = int(input("Liinide omavaheline max. kaugus (m): "))

if liinGap > liinTotal:
    print(2)
else:
    print(math.ceil((liinTotal/liinGap+1)))