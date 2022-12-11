def loetleFilmid(a):
    vas = []
    file = open('filmid.txt',"r",encoding="UTF-8")
    read = file.read().splitlines()
    for rida in read:
        li = rida.split(" - ")
        if (li[1]) == a:
            vas.append(li[0])
    return(vas)
    file.close()
def lisaFilm(b,c):
    lis = str(b)+(" - ")+str(c)
    print(lis)
    f = open("filmid.txt","a",encoding="UTF-8")
    f.write("\n")
    f.write(lis)
    f.close()
def kustutaFilm(d):
    file = open('filmid.txt',"r",encoding="UTF-8")
    read = file.readlines()
    file.close()
    file = open('filmid.txt',"w",encoding="UTF-8")
    for rida in read:
        li = rida.split(" - ")
        if li[0] != d:
            file.write(rida)

    file.close()
    file.close()