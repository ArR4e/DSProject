f = open("filmid.txt", "r+", encoding="utf8")
for rida in f:
    loen = f.readline()
    järjend = loen.split("-")
    
    def loetleFilmid(kategooria):
        if str(kategooria) in järjend:
            return järjend[0]
    def lisaFilm(film, zanr):
        a = f.write( film +' - '+ zanr+'\n')
    def kustutaFilm(film):
        if film in jäjend:
            järjend.remove()
            