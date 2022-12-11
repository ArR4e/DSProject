fail = input("Sisesta faili nimi: ")

f = open(fail)

bussid = []
for rida in f:
    bussid += [rida.strip().split(" ")]

sobivad = []
for buss in bussid:
    sobib = True
    for buss2 in bussid:
        if buss[0] < buss2[0] and buss[1] > buss2[1] and int(buss[2]) > int(buss2[2]):
            sobib = False

    if sobib:
        sobivad += [buss]
        
sobivad.sort()
for buss in sobivad:
    print(" ".join(buss))
f.close()