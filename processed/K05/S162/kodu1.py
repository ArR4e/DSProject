kasutajanimi=input("sisesta kasutajanimi: ")
while True:
    parool=input("sisesta parool: ")
    parool2=input("sisesta parool uuesti: ")
    if parool==parool2:
        if len(parool)<8:
            print("parool on liiga lühike")
        elif parool.isalpha()==True:
            print("Kasuta tähti ja numbreid")
        elif parool.isdigit()==True:
            print("Kasuta tähti ja numbreid")
        else:
            f=open("users.txt", "w")
            f.write(kasutajanimi+":"+parool[::-1])
            f.close()
            break
    else:
        print("need paroolid ei kattu")
