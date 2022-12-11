def loetleFilmid(zanr):
    f = open("filmid.txt", encoding="UTF-8")
    list1 = []
    for rida in f:
        rida = rida.strip("\n")
        if zanr in rida:
            rida = rida.strip(zanr)
            rida = rida.strip(" - ")
            list1.append(rida)
    return(list1)
    f.close()

def lisaFilm(nimi, zanr):
    f = open("filmid.txt", "a", encoding="UTF-8")
    list2 = [nimi," - ", zanr]
    str1 = "\n "
    for ele in list2:
        str1 += ele
    f.write(str1)
    f.close()

def kustutaFilm(nimi):
    with open("filmid.txt", "r", encoding="UTF-8") as file:
        read = file.readlines()
        
    with open("filmid.txt", "w", encoding="UTF-8") as file:
        for rida in read:
            if rida.find(nimi) != -1:
                pass
            else:
                file.write(rida)
    file.close()