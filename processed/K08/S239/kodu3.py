from film import *

def töötleKäsk(käsk,argument):
    if käsk == "K":
        if len(loetleFilmid(argument)) == 0:
            print("Soovitud žanris filmid puuduvad")
        else:
            print(loetleFilmid(argument))
        return True
    if käsk == "L":
        lisaFilm(argument[1],argument[0])
        print("Film lisatud!")
        return True
    if käsk == "V":
        kustutaFilm(argument)
        print("Film nimekirjast kustutatud!"+"\n"+"Head vaatamist!")
    
print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>"+
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")
while True:
    sisend = input()
    if sisend == "E":
        False
        break
    uus_sisend = []
    for i in sisend.split(" "):
        uus_sisend.append(i)
    käsk = uus_sisend[0]
    if käsk == "K":
        argument = uus_sisend[1]
    if käsk == "L":
        argument = []
        argument.append(uus_sisend[1])
        del uus_sisend[0:2]
        str1= " "
        argument.append(str1.join(uus_sisend))
    if käsk == "V":
        str1= " "
        argument = str1.join(uus_sisend[1:])
    töötleKäsk(käsk,argument)
        
    
        

