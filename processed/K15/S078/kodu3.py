failinimi = str(input('Sisestage failinimi: '))

with open(failinimi, 'r', encoding = 'UTF-8') as file:
    jarjend = []
    text = file.readlines()
    text.sort()
    for rida in text:
        vahe_rida = rida.strip('\n').split(' ')
        va = vahe_rida[0]
        sa = vahe_rida[1]
        tasu = float(vahe_rida[2])
        for rida2 in text:
            vahe_rida2 = rida2.strip('\n').split(' ')
            va2 = vahe_rida2[0]
            sa2 = vahe_rida2[1]
            tasu2 = float(vahe_rida2[2])
            if va < va2 and sa2 < sa and tasu2 < tasu:
                jarjend.append(rida)
    for lopp in text:
        if lopp not in jarjend:
            print(lopp.strip())