nimi = input('Sisesta failinimi: ')
f = open(nimi, encoding = 'utf-8')

bussid = []
for rida in f:
    buss = rida.strip().split()
    bussid += [buss]
  
for i in range(len(bussid)):
    min = i
    for j in range(i+1, len(bussid)):
        if bussid[j][2] < bussid[min][2]:
                min = j
    if i != min:
            bussid[i], bussid[min] = bussid[min], bussid[i]

hind = bussid[-1][2]
for i in range(len(bussid)):
    if bussid[i][2] == hind:
        bussid.remove(bussid[i])
  
  
for i in range(len(bussid)):
    min = i
    for j in range(i+1, len(bussid)):
        if bussid[j][0] >= bussid[min][0]:
            if bussid[j][1] <= bussid[min][1]:
                min = j
    if i != min:
            bussid[i], bussid[min] = bussid[min], bussid[i]
bussid.pop()

for i in range(len(bussid)):
    min = i
    for j in range(i+1, len(bussid)):
        if bussid[j][0] < bussid[min][0]:
                min = j
    if i != min:
            bussid[i], bussid[min] = bussid[min], bussid[i]



s = ' '

for i in bussid:
    print(s.join(i))
        

    
    
    
f.close()