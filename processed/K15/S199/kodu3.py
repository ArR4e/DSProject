
import re

fail = input("Sisesta failinimi: ")
f = open("bussiajad.txt")

bussid = []

for rida in f:
    buss = []
    tunnid = re.search("..:.. ..:..", rida)
    algus, lõpp = tunnid.group(0).split(" ")
    for algus, lõpp:
        tunnid, minutid = 
