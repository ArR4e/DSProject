def loetleFilmid(zanrinimi):
    j1 = []
    f = open("filmid.txt", 'r', encoding = "UTF-8")
    for el in f:
        if len(el.split(" - ")) == 2:
            filminimi = el.split(" - ")[0].strip("\n")
            zanr = el.split(" - ")[1].strip("\n")
            if zanr == zanrinimi:
                j1.append(filminimi)
    return j1
    f.close()

def lisaFilm(filminimi, zanrinimi):
    f = open("filmid.txt", 'a', encoding = "UTF-8")
    f.write("\n" + filminimi + " - " + zanrinimi)
    f.close()
    
def kustutaFilm(filminimi):
    f = open("filmid.txt", 'r', encoding = "UTF-8")
    filminimed = []
    zanrinimed = []
    
    for el in f:
        eraldatud = el.split(" - ")
        nimi = eraldatud[0]
        zanr = eraldatud[1].strip("\n")
        filminimed.append(nimi)
        zanrinimed.append(zanr)
    
    f.close()
    
    f = open("filmid.txt", 'w', encoding = "UTF-8")
    for i in range(len(filminimed)):
        if filminimed[i] != filminimi:
            f.write(filminimed[i] + " - " + zanrinimed[i] + "\n")
    f.close()
    

# lisaFilm("mr bean", "komöödia")
# loetleFilmid("õudukas")