def võrdle(b1, b2):
    if b1[0] < b2[0] and b1[1] > b2[1] and float(b1[2]) > float(b2[2]):
        return True
    return False


fail = input('Sisesta failinimi: ')
with open(fail, encoding='utf-8') as f:
    plaanid = []
    for rida in f:
        rida = rida.strip().split(' ')
        plaanid.append(rida)

uus = []
for buss1 in plaanid:
    sobib = True
    for buss2 in plaanid:
        if võrdle(buss1, buss2):
            sobib = False
    if sobib:
        uus.append(buss1)
        
uus.sort()
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')
for i in uus:
    i = ' '.join(i)
    print(i)
