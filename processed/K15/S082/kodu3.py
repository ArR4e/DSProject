def sõidupikkus(kell1, kell2):
    kell1 = kell1.split(':')
    kell2 = kell2.split(':')
    #print(kell1, kell2)
    uus1 = int(kell1[0])*60 + int(kell1[1])
    uus2 = int(kell2[0])*60 + int(kell2[1])
    return uus2 - uus1

fail = str(input('Sisesta failinimi: '))
f = open(fail, 'r')
nimekiri = []
#kõik üheks listiks
for a in f:
    a = a.strip()
    a = a.split()
    a += [str(sõidupikkus(a[0], a[1]))]
    nimekiri.append(a)

output = sorted(nimekiri, key=lambda x: x[-1])
#print(output)

esimene = output[0][-1]
vähimad = []
for a in output:
    if a[-1] == output[0][-1]:
        vähimad.append(a)
    elif a[-1] == vähimad[-1][-1]:
        vähimad.append(a)
    else:
        break
#print(vähimad)
l = []
e = vähimad[0][-2]
for a in vähimad:
    if a[-2] == vähimad[0][-2]:
        l.append(a)
    elif a[-2] == vähimad[-1][-2] or int(a[-2])-1 == int(vähimad[-1][-2]) or int(a[-2])-1 == int(vähimad[-1][-2]):
        l.append(a)
    else:
        break
    
#print(l)
'''
l = []
e = output[0][-2]
for a in output:
    if a[-2] == output[0][-2]:
        l.append(a)
    elif a[-2] == output[-1][-2] or int(a[-2])-1 == int(output[-1][-2]) or int(a[-2])-1 == int(output[-1][-2]):
        l.append(a)
    else:
        break
esimene = l[0][-1]
vähimad = []
for a in l:
    if a[-1] == l[0][-1]:
        vähimad.append(a)
    elif a[-1] == l[-1][-1]:
        vähimad.append(a)
    else:
        break
'''
#print(vähimad)
print('Esimeseest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
for a in vähimad:
    print(str(a[0] + ' ' + a[1]) + ' ' + a[2])



#print(nimekiri)