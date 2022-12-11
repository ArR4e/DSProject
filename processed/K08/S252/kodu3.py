from film import *

def töötlekäsk(kasuTahis,argumendid):
    if kasuTahis.upper() == "K":
        filmid = loetleFilmid(kaskArr[1])
        print("Võimalikud filmid on: ")
        i=0
        while i < len(filmid):
            print(filmid[i])
            i +=1
        print("")
        return True
    elif kasuTahis.upper() == "L":
        lisafilm(argumendid[1],argumendid[0])
        print("Film lisatud!")
        print("")
        return True
    elif kasuTahis.upper() == "V":
        kustutaFilm(argumendid[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        print("")
        return True
    elif kasuTahis.upper() == "E":
        return False
    else:
        print("")
        return True
    
print("Kuva filmid: K <žanr>")
print("Lisa film: L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta: E")

jätka = True
while jätka:
    sisend = input("")
    kaskArr = sisend.spilt("")
    kask = [0]
    arg1 = ""
    if (len(kaskArr)) > 1:
        arg1 = kaskArr[1]
    arg2=""
    i = 2
    while i < len(kaskArr):
        if i > 2:
            arg2 += ""
        arg2 += kaskArr[i]
        i +=1
        
    argumendid = ["",""]
    argumendid[0] = arg1
    argumendid[1] = arg2
    jätka = töötleKäsk(kask,argumendid)