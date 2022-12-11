fail = input("Sisesta faili nimi: ")
avafail = open(fail)
bussvälja = []
busskohal = []
busshind = []
sobivbuss = []

for rida in avafail:
    rida = rida.split(" ")
    bussvälja.append(rida[0])
    busskohal.append(rida[1])
    busshind.append(float(rida[2].strip()))


odavhind = min(busshind)
odavindex = busshind.index(odavhind)

sobivbuss.append(bussvälja[odavindex])
sobivbuss.append(busskohal[odavindex])
sobivbuss.append(busshind[odavindex])

print("Kõige odavam buss on", bussvälja[odavindex], busskohal[odavindex], busshind[odavindex], "Võib leiduda veel sama hinnaga busse, palun vaadake bussikava ise :)")
    

