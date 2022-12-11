#2. taksohinnad

f=open("taksohinnad.txt", encoding="utf-8")

pikkus=float(input("Sisesta tee pikkus kilomeetrites: "))

hinnad=[]
nimed=[]

for line in f:
    rida=line.replace(" ", "_")
    rida=rida.replace(",", " ")
    jupid=rida.split()
    nimi=str(jupid[0])
    nimed+=[nimi.replace("_", " ")]
    sisse=float(jupid[1])
    kilomeetri=float(jupid[-1])
    hind=sisse + kilomeetri*pikkus
    hinnad+=[(hind)]

if hinnad == []:
    hinnad+=[0]
    nimed+=["Pole infot"]

vastus=min(hinnad)
koht=hinnad.index(vastus)
firma=nimed[koht]

print("Kõige odavam on " + firma)

f.close()