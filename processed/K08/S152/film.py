def loetleFilmid(žanr):
    fail = open("filmid.txt", encoding="utf-8")
    järjend =[]
    for line in fail:
        sisu = line.strip().split(" - ")
        filmi_nimi = sisu[0]
        if sisu[1] == žanr:
            järjend.append(filmi_nimi)
    return järjend
    fail.close()
#mul automaatkontroll andis errori "UnsupportedOperation: not readable", aga mul endal loetleFilmid töötab
#loetleFilmid()
def lisaFilm(nimi,žanr):
    fail = open("filmid.txt", "a", encoding="utf-8")
    fail.write("\n" + nimi + " - " + žanr + "\n")
    fail.close()
    
def kustutaFilm(nimi):
    fail = open("filmid.txt", "w", encoding="utf-8")
    lisa = []
    for line in fail:
        sisu = line.strip().split(" - ")
        if nimi not in sisu:
            lisa.append(fail[0:2])
    fail.close()
    fail = open("filmid.txt", "w", encoding="utf-8")
    for filmike in lisa:
        fail.write(str(filmike[0]) + " - " + str(filmike[1]) + "\n")
    fail.close()
    
kustutaFilm("Shrek")
    
    
