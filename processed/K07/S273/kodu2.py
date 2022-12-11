f = open("taksohinnad.txt")

teepikkus = round(float(input("Sisesta tee pikkus kilomeetrites: ")))
maksumus = [] 
for rida in f:
    #maksumus = []
    #takso = f.readline().strip()
    #takso_list = takso.split(",")
    list = rida.strip().split(",")
    if float(list[-1]) == 0:
        hind = float(list[1])
    else:
        hind = float(list[1]) + teepikkus * float(list[2])
    maksumus.append(hind)
    #print(maksumus)

if maksumus[0] < maksumus[1] and maksumus[0] < maksumus[2]:
    print("Kõige odavam on Maksitaksi.")
if maksumus[1] < maksumus[0] and maksumus[1] < maksumus[2]:
    print("Kõige odavam on Sõps.")
if maksumus[2] < maksumus[0] and maksumus[2] < maksumus[1]:
    print("Kõige odavam on Waldo takso.")

f.close()