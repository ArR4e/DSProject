def loetleFilmid(genre):
    nimed = []
    f1 = open("filmid.txt", 'r', encoding = "utf-8")
    for rida in f1:
        nimi = rida.split(" - ")[0]
        zoom = rida.split()[-1]
        if genre == zoom:
            nimed.append(nimi)
    return nimed
    f1.close()
    
def lisaFilm(name, tyyp):
    with open("filmid.txt", 'a') as f1:
        kirjeldus = name + " - " + tyyp
        f1.write("\n")
        f1.write(kirjeldus)
        f1.write("\n")
    f1.close()

def kustutaFilm(name):
    with open("filmid.txt") as f1:
        x = []
        for rida in f1:
            o = f1.readline()
            x.append(o)
    f1.close()
    
    with open("filmid.txt", "w") as f1:
        for rida in x:
            nimi = rida.split(" - ")[0]
            if not nimi == name:
                f1.write(rida)
    f1.close()        
        
            
    
x = input("Sisestage siia filmižanr: ")
plot = loetleFilmid(x)
print(plot)

###ainult eraldi kasutamiseks

#y = input("Sisesta siia oma filmi nimi: ")
#lisaFilm(y, x)
#kustutaFilm(y)