a=float(input("Sisesta liini pikkus (täisarvuna) meetrites:"))
b=float(input("Sisesta maksimaalne postidevaheline kaugus (täisarvuna) meetrites:"))
import math
if a > b:
    print("Liini ehitamiseks on vaja minimaalselt:", math.ceil(a/b + 1), "posti")
if a == b:
    print ("Liini ehitamiseks on vaja minimaalselt: 2", "posti")
if a < b:
    print("Liini ehitamiseks on vaja minimaalselt: 2", "posti")