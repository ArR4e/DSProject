from math import *

pikkus = int(input("Palun sisestage ehitatava liini pikkus täisarvuna meetrites: "))
kaugus = int(input("Palun sisestage postide kaugus üksteisest täisarvuna meetrites: "))

postid = ceil(pikkus / kaugus) + 1

print ("Vastus: " + str(postid))