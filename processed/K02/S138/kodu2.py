import math
x = int(input("Sisestage elektriliini pikkus:"))
y = int(input("Sisestage maksimaalne postidevaheline kaugus:"))
z = math.ceil(x/y+1)
print(str(z)+" posti on vaja minimaalselt elektriliini püstitamiseks.")