def loetleFilmid(žanr):
    filmid1 = []
    f1 = open('filmid.txt','r')
    for rida in f1:
        järjekord = rida.strip().split(" - ")
        if str(järjekord[1]) == žanr:
            filmid1 += [järjekord[0]]
    f1.close()
    return filmid1

def lisaFilm(nimi,žanr):
    f2 = open('filmid.txt','a')
    filmid2 = ("\n" + nimi + " - " + žanr)
    f2.write(filmid2)
    f2.close()
    
def kustutaFilm(nimi):
    f3 = open('filmid.txt','r')
    filmid3 = []
    r = 0
    for rida in f3:
        sellel_real = rida.strip().split(" - ")
        if str(sellel_real[0]) == nimi:
            continue
        else:
            filmid3 += sellel_real
    f4 = open('filmid.txt','w')
    n = len(filmid3) - 1
    while n > r:
        sisu = (filmid3[r] +" - "+filmid3[r+1] +"\n")
        f4.write(sisu)
        r += 2
    f3.close()
    f4.close()