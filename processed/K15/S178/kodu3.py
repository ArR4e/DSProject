fail = input('Sisesta failinimi: ')
f = open(fail)
a = []
b = []
c = []
for rida in f:
    sisu = rida.split(' ')
    b.append(rida.strip())
    start = sisu[0].split(':')
    start1 = int(start[0])*60
    start2 = int(start[1])
    lõpp = sisu[1].split(':')
    lõpp1 = int(lõpp[0])*60
    lõpp2 = int(lõpp[1])
    maksumus1 = sisu[2].split('\n')
    maksumus = maksumus1[0]
    a.append(lõpp1 + lõpp2 - (start1+start2))

min = 100000000
for i in range(len(a)):
    if a[i] <= min:
        min = a[i]

for i in range(len(a)):
    if a[i] == min:
        c.append(b[i])
        
if len(c)==1:
    min2 = 100000000
    for i in range(len(a)):
        if a[i] <= min2 and min != a[i]:
            min2 = a[i]
    for i in range(len(a)):
        if a[i] == min2:
            c.append(b[i])

#print(c.sort())
from operator import itemgetter
c.sort(key=itemgetter(0))
for rida in c:
    print(rida)


