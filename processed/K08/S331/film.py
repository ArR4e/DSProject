def loetleFilmid(žanr):
    f = open("filmid.txt")
    järjend = []
    while True:
        rida = f.readline().strip()
        if rida == "":
            break
        rida1 = rida.split(" - ")
        nimi = rida1[0]
        if žanr == rida1[-1]:
            järjend.append(nimi)
    return(järjend)
    f.close()
def lisaFilm(nimi2, žanr2):
    f = open("filmid.txt", "a")
    f.write("\n" + nimi2 + " - " + žanr2)
    f.close()
def kustutaFilm(nimi3):
    f = open("filmid.txt")
    nimed = []
    žanrid = []
    while True:
        rida = f.readline().strip()
        if rida == "":
            break
        rida1 = rida.split(" - ")
        žanr = rida1[-1]
        if not rida1[0] == nimi3:
            nimed.append(rida1[0])
            žanrid.append(žanr)
    f.close()
    f = open("filmid.txt", "w")
    for i in range(len(nimed)):
        nimedžanriga = nimed[i] + " - " + žanrid[i]
        f.write(nimedžanriga + "\n")
    f.close()
        
