import math

a = int(input("Elektriliini pikkus täisarvuna meetrites on: "))
b = int(input("Kõrvutiasetsevale postide maksimaalne kaugus täisarvuna meetrites on: "))
x = float(a/b)
print ("Vaja on",(math.ceil(x)),"elektriposti.")