fail = open("filmid.txt","r",encoding="utf-8")
zanr = []
nimi = []
for i in fail.readlines():
    tükid = i.split(" - ")
    nimi= nimi+tükid[0:-1]
    zanr= zanr+[tükid[-1].strip("\n")]
fail.close()

def loetleFilmid(x):
    järjend=[]
    abi=0
    for i in zanr:
        if i == x:
            järjend=järjend+[nimi[abi]]
            abi+=1
        else:
            abi+=1
    return järjend
        
def lisaFilm(x,y):
    
    fail=open("filmid.txt","a",encoding="utf-8")
    fail.write("\n"+x+" - "+y)
    fail.close()
    
def kustutaFilm(x):
    fail=open("filmid.txt","r+",encoding="utf-8")
    for i in fail.readlines():
        nimi = []
        zanr = []
        tükid = i.split(" - ")
        nimi= nimi+tükid[0:-1]
        zanr= zanr+[tükid[-1].strip("\n")]
        if nimi != x:
            fail.write(i)
            continue
        else:
            continue
        fail.close()
