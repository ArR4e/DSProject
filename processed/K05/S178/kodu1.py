import re
kasutajanimi = str(input("Sisesta kasutajanimi: "))
parool1 = str(input("Sisesta parool: "))
parool2 = str(input("Sisesta parool uuesti: "))
sisestamisi = 1


while len(parool1) < 8 or parool1 != parool2 or not re.search("[0-99999999]",parool1) or not re.search("[a-z]",parool1) and not re.search("[A-Z]",parool1):
    print("Sisend pole korrektne")
    parool1 = str(input("Sisesta parool: "))
    parool2 = str(input("Sisesta parool uuesti: "))
    if sisestamisi == 1:
        break
    sisestamisi += 1 
    
tagurpidikasutajanimi = kasutajanimi[::-1]
tagurpidiparool = parool1[::-1]

f = open("user.txt", "w")
f.write("Kasutajanimi: " + tagurpidikasutajanimi + "        ")
f.write("Parool: " + tagurpidiparool)
f.close()
