#liini pikkus
x=int(input("Sisesta liini pikkus meetrites: "))
#kõrvutiasetsevate postide maksmaalkaugus
y=int(input("Sisesta postide maksimaalkaugus üksteisest meetrites: "))
from math import ceil
print("Vaja läheb minimaalselt "+str(ceil(x/y+1))+ " posti")