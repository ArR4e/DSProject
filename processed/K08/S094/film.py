# 1
def loetleFilmid(zanr):
    sobivad_filmid = []
    with open("filmid.txt", encoding="utf-8") as f:
        while True:
            loendur = f.readline().strip()
            if loendur == "":
                break
            
            # kas vastav zanr on real.
            if zanr in loendur:
                sobivad_filmid += [loendur]
            
    return sobivad_filmid        

# 2
def lisaFilm(nimi,zanr):
    # appendimine oleks mõistlik.
    with open("filmid.txt", "a",encoding="utf-8") as f:        
        f.write(nimi, "-", zanr)
        
# 3.. https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-file

def kustutaFilm(nimi):
    # loeme kogu olemasoleva sisu.
    with open("filmid.txt", "r",encoding="utf-8") as f:
        sisu = f.readlines()
        # scannime faili üle otsides nime.
        # kirjutame kõik read mida vaja uuesti aga seda
        # mida pole seda ei kirjuta.
        with open("filmid.txt", "w",encoding="utf-8") as f:
            for rida in sisu:
                # kirjutame kõik teised read va "nimi"
                if rida.strip("\n") != nimi:
                    f.write(rida)                                 
                    
