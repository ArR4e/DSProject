km = input("Sisesta tee pikkus kilomeetrites: ")

taksohinnad = open("taksohinnad.txt", "r")
_taksohinnad = taksohinnad.read().splitlines()
taksohinnad.close()

takso_1 = _taksohinnad[0]
takso_2 = _taksohinnad[1]
takso_3 = _taksohinnad[2]

_takso_1 =  takso_1.split(",")
_takso_2 =  takso_2.split(",")
_takso_3 =  takso_3.split(",")

hind_1 = (float(km)*float(_takso_1[2]))+float(_takso_1[1])
hind_2 = (float(km)*float(_takso_2[2]))+float(_takso_2[1])
hind_3 = (float(km)*float(_takso_3[2]))+float(_takso_3[1])

nimi = ""
if min(hind_1, hind_2, hind_3) == hind_1:
    nimi = _takso_1[0]
elif min(hind_1, hind_2, hind_3) == hind_2:
    nimi = _takso_2[0]
else:
    nimi = _takso_3[0]

print(" Kõige odavam on " + nimi)