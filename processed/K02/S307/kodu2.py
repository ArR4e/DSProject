import math

a = int(input("Kui pikk on liin?"))
b = int(input("Mis on kõrvutiasetsevate postide maksimaalne kaugus"))

if a<=b:
    print("Liini ehitamiseks on vaja 2 posti")
else:
    print("Liini ehitamiseks on vaja minimaalselt", math.ceil(a/b + 1), "posti")