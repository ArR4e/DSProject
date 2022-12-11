def seosta_lapsed_ja_vanemad(f1, f2):
    f1 = open(f1, 'r')
    f2 = open(f2, 'r')
    lisa_sõnastik = {}
    uus_sõnastik = {}

    for i in f2:
        i = i.strip().split()
        lisa_sõnastik[i[0]] = i[1] + ' ' + i[2]
        
    for rida in f1:
        rida = rida.strip().split()
        nimi = lisa_sõnastik[rida[1]]
        
        if nimi in uus_sõnastik:
            uus_sõnastik[nimi].add(lisa_sõnastik[rida[0]])
        else:
            uus_sõnastik[nimi] = set()
            uus_sõnastik[nimi].add(lisa_sõnastik[rida[0]])
    f1.close()
    f2.close()
    return uus_sõnastik
sõnastik = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for i in sõnastik:
    print(str(i) + ': ' + str(', '.join(list(sõnastik[i]))))