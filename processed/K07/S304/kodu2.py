teepikkus = float(input("Sisesta teepikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding="UTF-8")


for rida in f:
    rida = rida.split(',')
    takso = rida[0]
    tasu_algus = rida[1]
    km_hind = rida[-1]
    hind1 = float(tasu_algus) + float(km_hind.strip()) * teepikkus
    break

for rida2 in f:
    rida2 = rida2.split(',')
    takso2 = rida2[0]
    tasu_algus2 = rida2[1]
    km_hind2 = rida2[-1].strip()
    hind2 = float(tasu_algus2) + float(km_hind2.strip()) * teepikkus
    break

for rida3 in f:
    rida3 = rida3.split(',')
    takso3 = rida3[0]
    tasu_algus3 = rida3[1]
    km_hind3 = rida3[-1].strip()
    hind3 = float(tasu_algus3) + float(km_hind3.strip()) * teepikkus
    break

if hind1 == min([hind1, hind2, hind3]):
    print(f"Kõige odavam on {takso} ")

if hind2 == min([hind1, hind2, hind3]):
    print(f"Kõige odavam on {takso2} ")

if hind3 == min([hind1, hind2, hind3]):
    print(f"Kõige odavam on {takso3} ") 
    

    









