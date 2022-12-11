pikkus = float(input("Palun sisesta liini pikkus meetrites: "))
kaugus = int(input("sisesta maksimaalne postidevaheline kaugus meetrites: "))
import math

a = str(math.ceil(pikkus / kaugus) +1)

if pikkus >= 0 and kaugus >= 0:
    print("liini ehitamiseks on vaja " + a + " posti")

else:
    print("ebasobiv sisend")