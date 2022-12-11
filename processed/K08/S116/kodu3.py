from film import loetleFilmid, lisaFilm, kustutaFilm

while True:
    Sisend = (input("Sisesta käsk: "))

    nimekiri = Sisend.split(" ")
    käsk = nimekiri[0]
    muu = nimekiri[1:]
    def töötleKäsk(käsk, muu):

        if nimekiri[0] == "K":
            print(loetleFilmid(nimekiri[1]))
    
        elif nimekiri[0] == "L":
            lisaFilm(nimekiri[2], nimekiri[1])
    
        elif nimekiri[0] == "V":
            kustutaFilm(nimekiri[1])
    
        elif nimekiri[0] == "E":
            return False
        
        return True
    if töötleKäsk(käsk,muu) == False:
        break
    else:
        continue