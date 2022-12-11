pikkus = float(input("Sisesta tee pikkus kilomeetrites: "))

price = []
taksod = []

f = open("taksohinnad.txt", encoding = 'UTF-8')

for rida in f:
    line = rida.strip()
    line1 = line.split(',')
    taksod.append(line1[0])
    hind = float(line1[1]) + pikkus * float(line1[2])
    price.append(hind)
      
if price != []:
    x = min(price)
    odavaim_takso = price.index(x)
    print("Kõige odavam on", taksod[odavaim_takso])

f.close()
