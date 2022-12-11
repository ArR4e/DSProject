failinimi = str(input('Sisesta failinimi: '))

fail = open(failinimi, 'r+')
read = fail.readlines()
fail.seek(0)

for rida1 in read:
    sobib = True
    j = rida1.strip('\n').split()
    saeg1 = j[0]
    vaeg1 = j[1]
    hind1 = j[2]
    for rida2 in read:  
        j = rida2.strip('\n').split()
        saeg2 = j[0]
        vaeg2 = j[1]
        hind2 = j[2]
        
        if saeg1 <= saeg2 and vaeg1 >= vaeg2 and int(hind1) > int(hind2):
            if saeg1 == saeg2 and vaeg1 == vaeg2 and hind1 <= hind2:                              
                sobib = True
            else:
                sobib = False
                break
    
    if sobib:
        fail.write(rida1)
        
fail.truncate()

# paneme faili õigesse järjekorda
fail.seek(0)
read = fail.readlines()
while True:
    swap = False # tsükkel töötab kuni ühtegi vahetust enam ei toimu 
    for i in range(len(read)-1):
        j1 = read[i].split()
        j2 = read[i+1].split()
        vaeg1 = j1[0].split(':')
        vaeg2 = j2[0].split(':')
        if vaeg1[0] > vaeg2[0]: # kui y1 > y2, vahetus
            swap = True
            el1 = read[i]
            el2 = read[i+1]
            read[i+1] = el1
            read[i] = el2
        elif vaeg1[0] == vaeg2[0]: # kui y1 = y2, kontrollime x
            if vaeg1[1] > vaeg2[1]: # kui x1 > x2, vahetus
                swap = True
                el1 = read[i]
                el2 = read[i+1]
                read[i+1] = el1
                read[i] = el2  
    if swap == False:
        break

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ')

for rida in read:
    rida = rida.strip('\n')
    print(rida)

fail.close()
