import re

file = open("taksohinnad.txt", "r")
nimi = []
sisse_hind = []
km_hind = []
mitu = 0
odavam = ""

km = float(input("Mitu km koju:"))

file_sisu = file.read()
if file_sisu == "":
    quit()
file_sisu = file_sisu.split("\n")
for i in file_sisu:
    b = i.split(",")
    nimi.append(b[0])
    sisse_hind.append(b[1])
    km_hind.append(b[2])
    
mitu = len(nimi)
compeditor = 0
liider = 100000
while mitu > 0:
    compeditor = float(sisse_hind[mitu-1]) + float(km_hind[mitu-1]) * km
    if compeditor < liider:
        liider = compeditor
        odavam = nimi[mitu-1]
    mitu += -1
print("Kõige odavam on " + odavam + ".")
file.close()