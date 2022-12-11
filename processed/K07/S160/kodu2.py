### Kopeerisin 6pikust funktsiooni ymber kirjutamiseks ja korrigeerimiseks


#hinnakiri = open("taksohinnad.txt")
vahemaa = float(input("Mitu kilomeetrit soovite te s6ita? "))
#Loetakse rida rea haaval nõnda, et järjend koosneb 3st elemendist, [nimi, sisseistumise hind, kilomeetrihind].
#Et seda teha, tuleb mul teha funktsioon, mis arvutab v2lja, kui palju maksab inputitud vahemaa igal taksofirmal ja l6pus
#v2ljastab odavaima takso firma aka min(hind).


def hinnakiri(failinimi):
    firmanimi = []
    sisseastumine= []
    kilomeeter = []
    maksumus = 0
    f = open("taksohinnad.txt")
    for rida in f:
        osad = rida.split(" ")
        firmanimi = osad[0]
        sisseistumine = osad[1]
        kilomeeter = osad[2]
        
        maksumus = float(sisseistumine) + float(kilomeeter) * float(vahemaa)
        
    f.close()
    return (firmanimi, maksumus)

# salvestan enniku komponendid muutujatesse
(firmanimi, sisseistumine, kilomeeter) = hinnakiri("taksohinnad.txt")
print("Sisestatud vahemaa oli :" + float(str(vahemaa)))
print("Odavaim taksofirma selleks s6iduks on: " + nimi)
print("S6idu hind oleks:" + float(maksumus))