def loetleFilmid(teema):
    fail=open("filmid.txt")
    filmid=[]
    for rida in fail:
        järjend=rida.split("- ")
        nimi=järjend[0].strip()
        žanr=järjend[1].strip()
        if žanr == teema:
            filmid += [nimi]
    fail.close()
    return filmid

def lisaFilmid(nimi, teema):
    fail=open("filmid.txt", "a")
    fail.write("\n "+nimi+" - "+teema)
    fail.close()

def kustutaFilmid(nimi):
    algusfail=open("filmid.txt", "r")
    line=algusfail.readlines()
    algusfail.close()
    uusfail=open("filmid.txt", "w")
    for rida in line:
        järjend=rida.split(" - ")
        filminimi=järjend[0].strip()
        if nimi != filminimi:
            uusfail.write(rida)   
    uusfail.close()