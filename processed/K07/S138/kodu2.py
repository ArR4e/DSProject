f = open("taksohinnad.txt")
sisu = f.read()
sisu = sisu.replace("\n",",")

tee_pikkus = float(input("Sisesta tee pikkus kilomeetrites:"))
list = []
s = ""
for i in sisu:
    if i == ",":
        list.append(s)
        s = ""
    else:
        s+=i

a = 0
b = 1
c = 2
ohind = 0
odav_takso_nimi = ""
for i, x in enumerate(list):
    if i == a:
        odav_takso_nimix = x
        a+=3
    elif i == b:
        sisse_tasu = x
        b+=3
    elif i == c:
        kilomeetri_tasu = x
        hind = float(sisse_tasu) + float(kilomeetri_tasu)*tee_pikkus
        if ohind == 0 or hind < ohind:
            ohind = hind
            odav_takso_nimi = odav_takso_nimix
        c+=3
      
print("Kõige odavam on "+odav_takso_nimi)