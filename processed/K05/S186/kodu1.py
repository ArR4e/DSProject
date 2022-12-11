kasutajanimi=input("Sisestage kasutajanimi: ")
while True:
    parool1=str(input("Sisestage parool: "))
    parool2=str(input("Sisestage parool uuesti: "))
    if parool1!=parool2:
        print("Paroolid ei kattu, proovige uuesti.")
    else:
        if len(parool1)<8:
            print("Parool on liiga lühike, proovige uuesti.")
        else:
            if int(''.join(filter(str.isdigit, parool1)))>0:
                stringlength=len(parool1)
                slicedString=parool1[stringlength::-1]
                
                f=open("users.txt", "w+")
                f.write(kasutajanimi, ".", slicedString)
                f.close()