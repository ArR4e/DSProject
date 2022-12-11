fail=input("Sisesta fail: ")
f=open(fail,encoding='UTF-8')
sõiduplaan=[]
for rida in f:
    rida=rida.strip().split(' ')
    rida[2]=int(rida[2])
    sõiduplaan.append(rida)
f.close()
sobivad=[]
for i in sõiduplaan:
    for j in sõiduplaan:
        if i[0]>j[0]:
            if i[1]<j[1]:
                if i[2]<j[2]:
                    if i not in sobivad:
                        sobivad.append(i)
        else:
            if i[1]<j[1]:
                if i[2]<j[2]:
                    if i not in sobivad:
                        sobivad.append(i)
for rida in sobivad:
    print(rida[0], rida[1], rida[2])