from math import *

f = open("kinganumbrid.txt")
while True:
    kinganumber = f.readline()
    
    try:
        kinganumber == ""
        break
    try:
        kinganumber == float(kinganumber)
        pikkus = (2 / 3 * (kinganumber - 2))
        print(pikkus)
        break
        
    except: 
        print("Viganes sisend.")

    