kasutajanimi = str(input("Sisestage kasutajanimi: "))
while True:
    parool1 = str(input("Sisestage oma parool: "))
    parool2 = str(input("Sisestage oma parool teist korda: "))
    if parool1 == parool2:
        pass
    else:
        print("Sisestatud paroolid ei kattu")
        continue
    if len(parool1) >= 8:
        pass    
    else:
        print("Sisestatud parool on liiga lühike")
        continue
        
    if parool1.isalpha() or parool1.isnumeric():
        print("Sisestatud parool ei sisalda numbreid ja tähti mõlemaid")
        continue
    else:
        break
    
ümberpööratud = ''.join(reversed(parool1))
sisend = (kasutajanimi + ":" + ümberpööratud)

x = open("users.txt", "w")
x.write(str(sisend))
x.close()
print("Kasutaja on loodud")
    

