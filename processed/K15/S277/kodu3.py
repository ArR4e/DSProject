nimi = input('Sisesta failinimi: ')
f = open(nimi, 'r')
read = f.read().split('\n')
bussid = []

for rida in read:
    bussid += [rida.split()]
    
def vordlus():
    head = []
    for buss1 in bussid:
        valj1 = int(buss1[0].split(':')[0]) * 60 + int(buss1[0].split(':')[1])
        saab1 = int(buss1[1].split(':')[0]) * 60 + int(buss1[1].split(':')[1])
        kogu1 = saab1 - valj1
        for buss2 in bussid:
            valj2 = int(buss2[0].split(':')[0]) * 60 + int(buss2[0].split(':')[1])
            saab2 = int(buss2[1].split(':')[0]) * 60 + int(buss2[1].split(':')[1])
            kogu2 = saab2 - valj2
            
            if kogu1 < kogu2:
                if buss1 not in head:
                    head += [buss1]
            
    return head

head = vordlus()
for i in head:
    head[(head.index(i))] = ' '.join(i)
    
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')
print('\n'.join(head))




