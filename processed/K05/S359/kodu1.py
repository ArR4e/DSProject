knimi=str(input("Sisestage kasutajanimi:"))

while True:
    parool=str(input("Sisestage parool:"))
    parool1=str(input("Palun sisetage parool uuesti:"))
    a=parool.isalpha()
    b=parool.isnumeric()
    if parool == parool1:
        pass
    else:
        print("Paroolid ei kattu!")
        continue
        #raise Exception("Teine parool ei kattu esimese parooliga!")
    if len(parool)>=8:
        pass
    else:
        print("Parool peab olema pikem kui 8 tähemärki!")
        continue
    if a is True or b is True:
        print("Parool peab sisaldama nii tähti kui ka numbreid!")
        continue
    else:
        break

tagurpidi=parool[::-1]
koik=knimi+":"+tagurpidi
f=open("users.txt", "w")
f.write(koik)
f.close()
