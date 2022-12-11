from film import loetleFilmid
from film import lisaFilm
from film import kustutaFilm
a=input("Sisesta tähis: ")
b=[]
def töötleKäsk(a, b):
    if a == ("K"):
        return(loetleFilmid(b[0]))
    if a == ("L"):
        return(lisaFilm(b[1]))
    if a == ("V"):
        return(kustutaFilm(b[2]))
    if a == ("E"):
        c=input("Kas soovid lõpetada?")
        if c == ("Jah"):
            return False
        if c == ("Ei"):
            return True
    
    
töötleKäsk(a, b)