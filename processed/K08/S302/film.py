def loetleFilmid(zanr):
    filmid = []
    fail = open("filmid.txt", encoding = "utf-8")
    read = fail.readlines()
    fail.close()
    k = 0
    while k < len(read):
        zan = read[k].strip().split(" - ")
        if zan[1] == zanr:
            filmid.append(zan[0])
        k += 1
    
    return(filmid)
    
def lisaFilm(nimi, zan):
    fail = open("filmid.txt", "a", encoding = "utf-8")
    lisa = nimi + " - " + zan
    fail.write("\n" + lisa)
    fail.close()

def kustutaFilm(nimi):
    fail = open("filmid.txt","r", encoding = "utf-8")
    read = fail.readlines()
    fail.close()
    sisu = []
    k = 0
    f = open("filmid.txt","w", encoding = "utf-8")
    for rida in read:
        lol = rida.strip().split(" - ")
        if lol[0] != nimi:
            f.write(rida)
    
#     while k < len(read):
#         jah = read[k].strip().split(" - ")
#         if jah[0] == nimi:
#             k = k
#         else:
#             sisu.append(jah)
#         k += 1
#     for el in sisu:
#         uus = (str(sisu[0]) + " - " + str(sisu[1]) + "\n")
#         fail.write(uus)
    f.close()