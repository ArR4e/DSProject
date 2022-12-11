marullist = []
multikalist = []
oudukalist = []
nimelist = []


def loetleFilmid(zanr):
    if zanr == 'mÃ¤rul':
        print(marullist)
    elif zanr == 'multikas':
        print(multikalist)
    elif zanr == 'Ãµudukas':
        print(oudukalist)
    else:
        print("Sellist zanrit süsteemis pole")
        
def lisaFilm(zanr,nimi):
    f = open("filmid.txt","r+")
    x = f.readlines()
    print(nimi,"-",zanr,file=f)
    f.close()
    
def kustutaFilm(nimi):
    f = open("filmid.txt","r+")
    x = f.readlines()
    global nimelist
    f.close()
    y = x.pop(nimelist.index(nimi))
    f = open("filmid.txt","r+")
    for i in range(len(x)):
        print(x[i].strip('\n'),file=f)
    f.close()
    
    
    
f = open("filmid.txt","r+")
while True:
    rida = f.readline()
    if rida == '':
        f.close()
        break
    ajutine = rida.strip("\n").split(" - ")
    print(ajutine[0])
    nimelist = nimelist + [ajutine[0]]
    if ajutine[1] == "mÃ¤rul":
        marullist = marullist + [ajutine[0]]
        #print(marullist)
    if ajutine[1] == "multikas":
        multikalist = multikalist + [ajutine[0]]
        #print(multikalist)
    if ajutine[1] == "Ãµudukas":
        oudukalist = oudukalist + [ajutine[0]]
        #print(oudukalist)
        
        