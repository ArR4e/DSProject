import math
a = int(input("Sisestage liini pikkus (meetrites): "))
b = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus (meetrites): "))

c = a/b #mitu posti on liini ehitamiseks vaja

print(math.ceil(c)+1) #ümardab