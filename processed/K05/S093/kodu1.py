nimi = input("Sisestage oma kasutajanime: ")

while True:
    parool_1 = input("Sisesta oma parooli: ")
    parool_2 = input("Sisesta parooli teist korda: ")
    
    if parool_2 != parool_1:
        print("Paroolid pole samad")
        continue
    
    if len(parool_2) < 8:
        print("Parool on liiga väike")
        continue
    
    if parool_2.isalpha() or parool_2.isnumeric():
        print("Parool peab sisaldama numbreid kui ka tähti")
        continue

    else:
        print("Andmed on salvestatud")
        break

f = open("users.txt", "w")
f.write(nimi + ":" + parool_2[::-1])
f.close()



