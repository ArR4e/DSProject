nimi=input("Kasutajanimi palun")
while True:
    parool1=input("Mis on parool?")
    parool2=input("Sisestage parool uuesti")
    if parool1==parool2:
        if len(parool1)>=8:
            if parool1.isalpha()==False and parool1.isnumeric()==False:
                break
            else:
                print("Teie parool peab sisaldama tähti ja numbreid")
        else:
            print("Teie parool pole piisavalt pikk, proovige uuesti")
    else:
        print("Teie paroolid ei kattu, proovige uuesti")
parool1=list(parool1)
parool1.reverse()
parool1="".join(parool1)
f=open("users.txt","w")
print(nimi+":"+parool1,file=f)
f.close()