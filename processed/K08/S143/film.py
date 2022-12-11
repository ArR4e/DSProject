def loetleFilmid(z):
    d = {}
    with open("filmid.txt", "r",encoding="UTF-8") as f:
        for line in f:
            line = line.strip().split(" - ")
            if line[1] not in d.keys():
                d[line[1]] = [line[0]]
            else:
                d[line[1]].append(line[0])
    #print(d)
    try:
        return(d[z])
    except:
        return([])

def lisaFilm(n,z):
    with open("filmid.txt", "a",encoding="UTF-8") as f:
        f.write('\n'+n+" - "+z)

def kustutaFilm(n):
    a = []
    with open("filmid.txt", "r",encoding="UTF-8") as f:
        for line in f:
            if n not in line.split(" - "):
                a.append(line)
    open("filmid.txt","w").close()
    with open("filmid.txt", "w",encoding="UTF-8") as f:
        for el in a:
            f.write(el)
#lisaFilm("test","märul")
#kustutafilm("test")
#print(loetleFilmid("märul"))