f=open("taksohinnad.txt", encoding= "utf-8")
a=float(input("Sisesta tee pikkus kilomeetrites: "))

hinnad=[]
nimed=[]

for rida in f:
    järjend = rida.split(",")
    
    nimi=järjend[0]
    nimed.append(nimi)
    
    sisseistumine=float(järjend[1])
    kmhind=float(järjend[2])
    hinnad.append(a*kmhind+sisseistumine)
    
odavaim = min(hinnad)
indeks = hinnad.index(odavaim)


print("Kõige odavam on", nimed[indeks] + ".")
    

f.close()