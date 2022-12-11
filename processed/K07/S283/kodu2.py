taksofail = open("taksohinnad.txt", encoding="UTF-8")

kodutee = float(input("Sisestage teepikkus koduni(km): "))

hind = 0
odavaim = 0
odavaim_takso = " "

for rida in taksofail:
    rida = rida.strip()
    järjend = rida.split(",")
    takso_nimi = järjend[0]
    sisseistumine = float(järjend[1])
    kilomeeter = float(järjend[2])
    hind = sisseistumine + round(kilomeeter * kodutee, 2)
    if hind < odavaim or odavaim == 0:
        odavaim = hind
        odavaim_takso = takso_nimi
    
if odavaim_takso == " ":
    print("Taksod on koju läinud.")
else:
    print("Kõige odavam on: " + odavaim_takso + ".")

taksofail.close()