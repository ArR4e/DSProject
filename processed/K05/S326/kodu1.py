kasutaja = str(input("Sisesta kasutajanimi: "))
def paroolcheck():
    while True:
        parool1 = str(input("Sisesta parool: "))
        parool2 = str(input("Sisesta parool uuesti: "))
        if parool1 != parool2:
            print("Parool ei kattu")
        elif len(parool1) < 8:
            print("Parool liiga lühike")
#https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
#Tagastab True kui stringis esineb number
        elif any(char.isdigit() for char in parool1) == False:
            print("Peab sisaldama numbreid ja tähti")
#Kontrollib et parool poleks ainult numbrid    
        elif parool1.isdigit() == True:
            print("Peab sisaldama numbreid ja tähti")
        else:
            break
    return(parool2)
#https://www.w3schools.com/python/python_howto_reverse_string.asp
paroolreverse = paroolcheck() [::-1]
f = open("users.txt", "w")
f.write(f"{kasutaja}:{paroolreverse}")
f.close()
