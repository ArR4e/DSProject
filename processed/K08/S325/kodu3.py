from film import *
def töötleKäsk(A,j):
    if A == "E":
        return False
    elif A == "K":
        l=loetleFilmid(j)
        if l==[]:
            print("Sellest žanrist filme pole!")
        else:
            print("\nVõimalikud filmid on:")
            for el in l:
                print(el)
        print("\n")
        return True
    elif A == "L":
        try:
            sanr=j.split()[0]
            film=""
            l=len(j.split())
            i=2
            while i<=l:
                film+=(j.split())[i-1]+" "
                i+=1
            film=film.strip()
            lisaFilm(film,sanr)
            print("Film lisatud!")
        except:
            print("Filmi lisamine ebaõnnestus, proovi uuesti!")
        return True
    elif A == "V":
        try:
            kustutaFilm(j)
            print("Film kustutatud!")
        except:
            print("Sellist filmi ei leitud andmebaasist, proovi uuesti!")
        return True
    else:
        return True
print("=== FILMIANDMEBAAS ===\nKuva filmid: K <žanr>\nLisa film:   L <žanr> <film>\nVaata filmi: V <filmi nimi>\nLõpeta:      E\n===")
cont=True
while cont == True:     
    käsk=str(input("Sisesta käsk:"))
    cont=töötleKäsk(käsk[0],käsk[2:])



#=== FILMIANDMEBAAS ===
#Kuva filmid: K <žanr>
#Lisa film:   L <žanr> <film>
#Vaata filmi: V <filmi nimi>
#Lõpeta:      E
#===