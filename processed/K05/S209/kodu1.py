def kontroll(x1, x2):
    if x1 != x2:
        return "Paroolid ei klapi"
    elif len(x1) < 8:
        return "Parool liiga lühike"
    kontroll1 = False
    kontroll2 = False
    for i in x1:
        if kontroll1 and kontroll2:
            return False         
        if i.isnumeric():
            kontroll1 = True
        elif i.isalpha():
            kontroll2 = True
        
    return "Parool peab sisaldama tähti ja numbreid"

nimi = input("Sisestage kasutajanimi: ")

salasona1 = input("Sisestage parool: ")
salasona2 = input("Sisesta parool: ")

if kontroll(salasona1, salasona2):
    print(kontroll(salasona1, salasona2))
        
while kontroll(salasona1, salasona2):
    
    salasona1 = input("Sisestage parool: ")
    salasona2 = input("Sisesta parool: ")
    if kontroll(salasona1, salasona2):
        print(kontroll(salasona1, salasona2))

salasona1 = salasona1[::-1]

f = open("users.txt", "w+")
f.write(nimi + " : " + salasona1)
f.close()