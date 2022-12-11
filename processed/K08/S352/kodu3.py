import film
välj=[]
i=True
def töötleKäsk(kask,jrj):
    global välj
    if kask=="K":
        välj=film.loetleFilmid(jrj[0])
        print(välj)
        #return välj
        return True
    elif kask=="L":
#         jrj=jrj.split(" ",2)
        film.lisaFilm(jrj[1],jrj[0])
        print("Film lisatud!")
        return True
    elif kask=="V":
        film.kustutaFilm(jrj[0])
        print("Film kustutatud")
        return True
    elif kask=="E":
        return False


while i==True:
    sisend=input("""
    === FILMIANDMEBAAS ===
    Kuva filmid: K <žanr>
    Lisa film:   L <žanr> <film>
    Vaata filmi: V <filmi nimi>
    Lõpeta:      E
    ======================
    """)

    sisend=sisend.split(" ",2)
    k=sisend[0]
    jrj=sisend[1:]

    i=töötleKäsk(k,jrj)
