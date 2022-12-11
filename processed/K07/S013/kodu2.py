f=open("taksohinnad.txt", encoding="UTF-8")
x =float(input("Sisesta tee pikkus kilomeetrites: "))

nimed = []
järjend = []
for rida in f:
    järjend1 = rida.strip()
    järjend1 = järjend1.split(",")
    nimi = järjend1[0]
    nimed.append(nimi)
   
    start = float(järjend1[1])
    tasu = float(järjend1[2])
    hind = str(start + (x * tasu))
    järjend.append(float(hind))

indeks = 0
miinimum = järjend[0]
for i in range(len(järjend)):
    if järjend[i] < miinimum:
        miinimum = järjend[i]
        indeks = i
   
print("Kõige odavam on " + str((nimed[indeks])))
f.close()