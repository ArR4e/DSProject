def loetleFilmid(žanr):
    f = open("filmid.txt", "r+", encoding="UTF-8")
    a = []
    for rida in f:
        järjend = rida.strip().split(" - ")
        if järjend == [""]:
            break
        if järjend[1] == žanr:
            a.append(järjend[0])
    return a
    f.close()
    
def lisaFilm(nimi, žanr):
    file=open("filmid.txt", "a", encoding="UTF-8")
    file.write(" \n")
    file.write(nimi)
    file.write(" - ")
    file.write(žanr)
    file.close()
    
def kustutaFilm(nimi):
    with open("filmid.txt", "r", encoding="UTF-8") as f:
        read = f.readlines()
    with open("filmid.txt", "w", encoding="UTF-8") as f:
        for rida in read:
            järjend = rida.strip("\n").split(" - ")
            if järjend[0] != nimi:
                f.write(rida)
    
   
         
    

