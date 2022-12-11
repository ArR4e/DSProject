f = open("filmid.txt","r+", encoding = "UTF-8")
multikas = "multikas"
märul = "märul"
õudukas = "õudukas"
rida = ""

def loetleFilmid(x):
    while True:
        rida = f.readline().strip("\n").split(" - ")
        if rida[0] == "":
            break
        else:
            if rida[1] == str(x):
                print(rida[0])


def lisaFilm(y, z):
    f = open("filmid.txt","a", encoding = "UTF-8")
    lisan = str(y)+" - "+str(z)
    f.write("\n")
    f.write(lisan)
    f.close()


def kustutaFilm(nimi):
    loen = open("filmid.txt", "r", encoding = "UTF-8")
    a = loen.readlines()
    loen.close()
    for el in a:
        if nimi in el:
            a.remove(el)
    f = open("filmid.txt", "w", encoding = "UTF-8")
    f.writelines(a)

loetleFilmid("õudukas")

        

