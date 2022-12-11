fail = open("filmid.txt", "r+")

filmi_nimi = []
filmi_žanr = []
for rida in fail:
    rida = rida.strip()
    järjend = rida.split(" - ")
    filmi_nimi.append(järjend[0])
    filmi_žanr.append(järjend[1])
    if rida == "":
        break
 
def loetleFilmid(žanr):
    nimi = []
    for i in range(len(filmi_žanr)):
        if filmi_žanr[i] == žanr:
            nimi.append(filmi_nimi[i])
    return nimi
            
def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a")
    fail.write("\n")
    fail.write(str(nimi) + " - " + str(žanr))
    fail.close()

def kustutaFilm(nimi):
    fail = open("filmid.txt", "r")
    read = fail.readlines()
    fail.close()
    fail = open("filmid.txt", "w")
    for rida in read:
        if rida.find(nimi) != -1:
            pass
        else:
            fail.write(rida)
    fail.close()
fail.close()
        