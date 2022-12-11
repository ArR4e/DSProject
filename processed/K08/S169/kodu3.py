from film import *

def töötleKäsk(käsk,järjend):
    if käsk == "E":
        return False
    else:
        if käsk == "K":
            print("Võimalikud filmid on:")
            for a in loetleFilmid(järjend[1]):
                print(a)
            return True
            
        elif käsk == "L":
            filmi_nimi = " "
            filmi_nimi = filmi_nimi.join(järjend[2:])
            lisaFilm(filmi_nimi,järjend[1])
            print("Film lisatud!")
            return True
            
        elif käsk == "V":
            filmi_nimi = " "
            filmi_nimi = filmi_nimi.join(järjend[1:])
            kustutaFilm(filmi_nimi)
            print("Film kustutatud, head vaatamist!")
            return True
              
print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\n\
Lisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\n\
Lõpeta:      E\n===")
a = True
while a == True:
    järjend = []
    filmi_nimi = " "
    sisend = input()
    sisend= sisend.split(" ")
    käsk = sisend[0]
    print(sisend)
    a = töötleKäsk(käsk, sisend)
    