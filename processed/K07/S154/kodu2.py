tee_pikkus = int(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt", encoding="UTF-8")
fail = f.readlines()
for el in fail:
    andmed = el.strip().split(",")
    if andmed == ["Maksitaksi", "2.0", "0.6"]:
        maksi = float("2.0") + float("0.6")*tee_pikkus
    elif andmed == ["Sõps veab", "10", "0"]:
        sõps = int("10") + int("0")*tee_pikkus
    else:
        waldo = float("1.0") + float("1.0")*tee_pikkus

    
          
f.close()

if maksi < sõps and maksi < waldo:
    print("Kõige odavam on Maksitaksi")
elif sõps < maksi and sõps < waldo:
    print("Kõige odavam on Sõps veab")
else:
    print("Kõige odavam on Waldo takso")