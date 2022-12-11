f = open("filmid.txt", "r+" , encoding="utf-8")
d = {}

for rida in f:
    x = rida.strip("\n").split(" - ")
    if x[1] in d:
        d[x[1]].append(x[0])
    else:
        d[x[1]]= [x[0]]

print(d)
def loetleFilmid(nimi):
     return d.get(nimi)
   
    

def lisafilm(nimi,zanr):
    return (nimi + " - " + zanr)
def kustutaFilm(nimi):
    lines = f.readlines()
    with open("filmid.txt", "w" , encoding="utf-8") as fd:
        for line in lines:
            if line.strip("\n").startswith(' '+ nimi):
                continue
            else:
                fp.write(line)
    fd.close()
    

f.close()
