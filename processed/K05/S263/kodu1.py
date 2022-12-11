import re

nimi = input("Sisesta kasutajanimi: ")
while True:
    parool_1kord = input("Sisesta parool: ")
    parool_2kord = input("Sisesta parool uuesti: ")
    i = False
    
    if parool_1kord != parool_2kord:
        print("Sisestatud paroolid ei ühti")
        continue
    elif len(parool_1kord) < 8:
        print("Sisestatud parool on liiga lühike")
        continue
    elif not re.search("[a-z]", parool_1kord):
        print("Parool peab sisaldama vähemalt ühte tähte")
        continue
    elif not re.search("[0-9]", parool_1kord):
        print("Parool peab sisaldama vähemalt ühte numbrit")
        continue
    else:
        i=True
        break
    
if True:
    #print("Sobilik parool")
    tagurpidi = parool_1kord.join(w[::-1] for w in parool_1kord.split())
    #print(tagurpidi)
    f=open("users.txt", "x")
    f.write(nimi + ":" + tagurpidi)
    #f.write(tagurpidi + "\n")
    f.close()
    
        
