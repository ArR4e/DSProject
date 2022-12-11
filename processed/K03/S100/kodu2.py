from pykkar import *

#Teen algse laua kasutaja käsu järgi
laius = int(input("Sisestage seinata seinata maailma laius(>2): "))+2
pikkus = int(input("Sisestage maailma pikkus(>2):"))+2

laudalg = '#'*laius+('\n#'+' '*(laius-2)+'#')*(pikkus-2)+'\n'+'#'*laius

#Teen uue laua, sest python sõnes asendamist ei luba, ning asetan lauda Pykkari kasutaja käsu järgi
print("NB! Laua 0, 0 koordinaadiks peetakse ülemist vasakpoolset nurka(alati sein)\nX- ning y-telg suurenevad vastavalt paremale ning alla ")
pykkarx = int(input("Sisestage Pykkari alguspunkti abtsiss: "))
pykkary = int(input("Sisestage Pykkari alguspunkti ordinaat: "))

laud = laudalg[:pykkary*(laius+1)+pykkarx]+'>'+laudalg[pykkary*(laius+1)+pykkarx+1:]

#Loon eelnevalt sisestatud parameetritega Pykkarile maailma
create_world(laud)

#Veendun, et Pykkar jõuab seinani, mida ta algusest peale vaatab
while(not is_wall()):
    step()
right()

#Kuna Pykkar on nüüd seina ääres, peab ta vaid kõndima otse, sest järgmine vastu tulev sein on nurk,
#järelikult peab ta lihtsalt selle ruudu, värvima, paremale keerama, ning seda tegema veel 3 korda.
for i in range(4):
    while(not is_wall()):
        step()
    paint()
    right()

exitonclick()