kasutaja = input('Sisesta oma kasutaja nimi')
pikkus = 0
z = 0
x = 0
y = 0
a = 0
while a < 1:
    parool = input('Sisesta oma parrol')
    parool1 = input('Sisestage ma praool uuesti')
    if parool == parool1:
        õige = 1
    else:
        õige = 0
    if õige == 0:
        print ('Parool ei ühti')
    elif len(parool) >=8:
        pikkus = 1
    else:
        pikkus = 0
    if pikkus == 0:
        print('Parool ei ole piisavalt pikk')
    for täht in parool:
        try:
            täht = int(täht)
            if type(täht) is str:
                x = x + 1
            if type(täht) is str:
                y = y + 1
        except:
            if type(täht) is str:
                z = z +1
    if x > 0 and y > 0:
        flip = 1
    else:
        flip = 0
    if õige + flip + pikkus == 3:
        a = 1
krüpto = parool[stringlength::-1]
fail = open('kasutajad.txt')
kiri = kasutaja + '-' + krüpto
fail.write(kiri)
fail.close()
        
        
        
