def numbridtähed (parool):
    täht = False
    number = False
    a= False
    for i in parool1:
        if i.isalpha():
            täht = True
        elif i.isnumeric():
            number= True
        if number == True and täht == True:
            a = True
        else:
            a = False
    return a

nimi = input("Sisesta kasutajanimi: ")
while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    pikkus = len(str(parool1))

    if parool1 == parool2 and pikkus >= 8 and numbridtähed(parool1) == True:
        break
    elif parool1 != parool2:
        print("Paroolid ei kattu.")
    elif pikkus < 8:
        print("Liiga lühike.")
    elif numbridtähed(parool1) == False :
        print("Parool peab sisaldama tähti ja numbreid.")

tulemus = ""
for i in reversed(parool1):
    tulemus = tulemus +i
f = open("users.txt", "w")
f.write(nimi + ":" + tulemus)
f.close()