def loetleFilmid(genre):
    with open("filmid.txt", "r+", encoding="UTF-8") as fail:
        loetelu = []
        for rida in fail:
            rida = rida.strip('\n')
            if str(genre) in rida:
                rida = rida.strip(genre)
                rida = rida.strip(' - ')
                loetelu += [rida]
        if loetelu == []:
            print("Sellise žanriga filmi ei leitud!")
        return loetelu

def lisaFilm(nimi, genre):
    with open("filmid.txt", "a+", encoding="UTF-8") as fail:
        film = ""
        film += nimi + " - " + genre
        fail.write("\n")
        fail.write(film)
    
    
def kustutaFilm(nimi):
    with open("filmid.txt", "r+", encoding="UTF-8") as fail:
        read = fail.readlines()
    with open("filmid.txt", "w+", encoding="UTF-8") as fail:
        for rida in read:
            if str(nimi) not in rida.strip("\n"):
                fail.write(rida)