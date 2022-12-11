f = open("taksohinnad.txt", encoding="UTF-8")
nimed = []
hinnad = []
hinnad3 = []
järjend = []

pikkus = float(input("Sisesta tee pikkus kilomeetrites: ")) 
for rida in f:
    jupid = rida.split(",")
    nimi = jupid[0]
    hind = jupid[1]
    hind2 = jupid[2].strip("\n")
    
    nimed.append(nimi)
    hinnad.append(hind)
    hinnad3.append(hind2)

hinnad2 = [float(x) for x in hinnad]

a = len(hinnad2)
hinnad4 = [float(x) for x in hinnad3]

for i in range(a):
    summa = hinnad2[i] + (hinnad4[i]*pikkus)
    #järjend.append(summa2)
    järjend.append(float(summa))

while True:
    try:
        väikseim = min(järjend)
        indeks = järjend.index(väikseim)
        print("Kõige odavam on " + str(nimed[indeks]))
        break
    except:
        break
