import film

def töötleKäsk(x,y):       

    if x == "K":
        if film.loetleFilmid(y) != []:
            print("Filmid antud zanrist on:"+"\n"+str(film.loetleFilmid(y)))
            return True
        else:
            print("polnud ühtegi sellisest zanrist")
            käsk=input("Sisesta käsu tähis ja käsk: ")
            tükid=käsk.split(" ")
            tähis=tükid[0]
            kask=tükid[-1]
            töötleKäsk(tähis,kask)
            return True
    elif x == "L":
        t=y.split(" ")
        k=t[0]
        l=t[-1]
        film.lisaFilm(k,l)
        return True
    elif x == "V":
        film.kustutaFilm(y)
        print(y+"\n"+"film nimekirjast kustutatud!"+"\n"+"Head vaatamist!")
        return True
    elif x == "E":
        return False 

käsk=input("Sisesta käsu tähis ja käsk: ")
tükid=käsk.split(" ")
tähis=tükid[0]
kask=tükid[-1]
töötleKäsk(tähis,kask)
