from math import *

f = open("kinganumbrid.txt", encoding = "utf-8")

while True:
    kinganumber = f.readline()
    
    if kinganumber == "":
        break
    
    try:
        kinga_number = float(kinganumber)
        print(round((2 / 3 * (kinga_number - 2))))
    except:
        print("Vigane sisend.")

f.close()
