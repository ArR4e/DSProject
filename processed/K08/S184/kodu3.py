import film
def töötleKäsk(käsk,järjend):
    while True:
        if käsk=="K":
            z=""
            x=järjend
            z="".join(x)
            k=film.loetleFilmid(z)
        elif käsk=="L":
            nimi=" "
            l=järjend
            zanr=l[0]
            del l[0]
            nimi=nimi.join(l)
            li=film.lisaFilm(nimi, zanr)
            print("Film on lisatud")
        elif käsk=="V":
            n=järjend
            n=n[-1]
            v=film.kustutaFilm(n)
            print("Film on kustutatud")
        käsk=input()
        käsk2=käsk.split(" ")
        käsk=käsk2[0]
        del käsk2[0]
        järjend=käsk2
        if "E" not in käsk :
            continue
        else:
             break

sisend=input()
sisend2=sisend.split(" ")
käsk=sisend2[0]
del sisend2[0]
järjend=sisend2
töötleKäsk(käsk, järjend)
