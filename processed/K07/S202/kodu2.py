#arvasin alguses, et autokontrolli failis muutuvad ainult numbrid, seetõttu pidin pool programmi ümber kirjutama

Teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding="utf-8")
taksodelist = []
hindadelist = []
for rida in f:

    realist = rida.split(",")
    Takso = realist[0]
    Sisseistumine = realist[1]
    KMHind = realist[2].strip("\n")
    
    
    Taksohind = float(Sisseistumine) + (float(Teepikkus)*float(KMHind))
    
    taksodelist.append(Takso)
    hindadelist.append(Taksohind)
    
    
#print(taksodelist)
#print(hindadelist)

SuuruseVõrdlus = (hindadelist)
if len(SuuruseVõrdlus) > 1:
    Väikseim = min(SuuruseVõrdlus) #okei see kodu2test4 on koolikiusamine 
    Mitmes = hindadelist.index(Väikseim)
    odavaim = taksodelist[Mitmes]
    print("Kõige odavam on", odavaim)

f.close()