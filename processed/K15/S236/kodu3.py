#3. Bussid

#failinimi = input('Sisesta failinimi: ')
failinimi = 'sõiduplaan.txt'

with open(failinimi) as fail:
    for rida in fail:
        rida = rida.split('\n')
        print(rida[0])
        #Ilmselt ei tasu esimesest linnast teise sõitmiseks valida bussi, mille väljumisaeg on varasem,
        #saabumisaeg hilisem ja sõidu hind suurem kui mõnel teisel bussil.
        
#p