def sõiduplaan(failinimi):
    
    fail = open(failinimi, encoding='utf-8')
    for rida in fail:
        sobib = True
        rida = rida.strip()
        algus1, lõpp1, kulu1 = rida.split(' ')
        for rida2 in fail:
            rida2 = rida2.strip()
            algus2, lõpp2, kulu2 = rida2.split(' ')
            if algus1 < algus2 and lõpp1<lõpp2 and int(kulu1)<=int(kulu2):
                sobib = True
        print(rida)
print(sõiduplaan(input('Sisesta faili nimi: ')))
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')

