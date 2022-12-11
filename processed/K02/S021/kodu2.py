from math import ceil
a = int(input("Palun sisestage liini pikkus meetrites: "))
b = int(input("Palun sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
c= ceil(a/b + 1)
print ("Minimaalne postide arv elektriliini rajamiseks on", c )