nimi = input('Sisesta failinimi: ')
fail = open(nimi, 'r')
read = fail.readlines()
fail.close()
sobivad_bussid = []
for i in range(len(read)):
    sobib = True
    buss1 = read[i].split()
    vahe1 = str(int(buss1[1][0:2]) - int(buss1[0][0:2])) + ':' + str(int(buss1[1][3:5]) - int(buss1[0][3:5]))
    for j in range(len(read)):
        buss2 = read[j].split()
        vahe2 = str(int(buss2[1][0:2]) - int(buss2[0][0:2])) + ':' + str(int(buss2[1][3:5]) - int(buss2[0][3:5]))
        if buss1 != buss2 and vahe1 > vahe2 and int(buss1[2]) > int(buss2[2]):
            sobib = False
    if buss1 not in sobivad_bussid:
        if sobib == True:
            sobivad_bussid += [buss1]
                        
sobivad_bussid.sort()
for aeg in sobivad_bussid:
    print(' '.join(aeg))