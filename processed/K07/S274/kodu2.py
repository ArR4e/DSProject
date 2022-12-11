tee = float(input("Sisesta tee pikkus kilomeetrites: "))

f = open('taksohinnad.txt', encoding = "UTF-8")

while True:
    rida = f.readline().strip()
    if rida == "":
        break
    else:
        sisu = rida.split(",")    
        maksumus = float(sisu[1]) + tee * float(sisu[2])
        nimi = sisu[0]
        print(sisu)
        print(maksumus)
        print(nimi)

f.close()
