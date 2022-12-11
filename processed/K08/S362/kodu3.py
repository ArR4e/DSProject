from film import*

def töötleKäsk(käsu_tähis, järjend):
    käsu_tähis=järjend[0].upper()
    f=open("filmid.txt", encoding="UTF-8")

    filmid_zanrid=[]
    for rida in f:
        filmid_zanrid=filmid_zanrid+[rida.strip().split(" - ")]
    #print(filmid_zanrid)
    zanrid=[]
    for el in filmid_zanrid:
        if el!=[""]:
            if el[1] not in zanrid:
                zanrid=zanrid+[el[1]]
#print(zanrid)
    
    f.close()
    
    if käsu_tähis=="K":
        zanr=järjend[1].lower()
        if zanr not in zanrid:
            print("Selle zanriga filme sul veel pole. Kui tahad, lisa.")
            vastus=True
        else:
            käsk=loetleFilmid(zanr)
            uus_list=[]
            for el in käsk:
                uus_list=uus_list+[(el+ "\n")]
            #print(uus_list)
            filmid="".join(uus_list)
            print("Võimalikud filmid on:")
            print(filmid)
            vastus=True
    elif käsu_tähis=="L":
        zanr=järjend[1].lower()
        nimi=" ".join(järjend[2:])
        käsk=lisaFilm(nimi, zanr)
        print("Film lisatud!")
        vastus=True
    elif käsu_tähis=="V":
        nimi=" ".join(järjend[1:])
        käsk=kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        vastus=True
    elif käsu_tähis=="E":
        #print("")
        vastus=False
#     f.close()
    return vastus
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")


while True:
    
    sisend=input(">")
    järjend=sisend.split(" ")
    käsu_tähis=järjend[0].upper()
#     zanr=järjend[1].lower()
#     nimi=" ".join(järjend[2:])
#     print(zanr)
#     print(käsu_tähis)
#     print(nimi)
    
    vastus=töötleKäsk(käsu_tähis, järjend)
    if vastus==False:
        break
    
        



    
# sisend=input(">")
# järjend=sisend.split(" ")
# käsu_tähis=järjend[0]
# zanr=järjend[1].lower()
# nimi=" ".join(järjend[2:])
# print(zanr)
# print(käsu_tähis)
# print(nimi)
# if käsu_tähis.isupper():
#     print(käsu_tähis)
# else:
#     print(" Käsutäht oli millegi pärast väike")
# print(zanr)
#         
