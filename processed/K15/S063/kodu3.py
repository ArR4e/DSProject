'''-- Kodutöö nr. 15 - 3. Bussid --'''
#############################################################################################
## Kirjuta programm, mis väljastab ekraanile väljumisaegade järjestuses kõik bussid,
## mil väljumisaeg on varasem, saabumisaeg hilisem ja sõidu hind suurem mõni teisest bussist.
from datetime import datetime
#############################################################################################
## funktsioon sorteerib väljumisaega järgi kasvavalt
def järjesta(bussid):
    
    for i in range(len(bussid)):
        min_indeks = i
        for j in range(i+1, len(bussid)):
            # kui on leitud väiksem väljumisaeg, siis vaheta ümber
            if bussid[j][0] < bussid[min_indeks][0]:
                min_indeks = j
        bussid[i], bussid[min_indeks] = bussid[min_indeks], bussid[i]
    
    return bussid
#############################################################################################
## funktsioon võrdleb iga bussi väljumisaega, saabumisaega ja hinda kõikide teiste bussidega
def võrdle(bussid):
    bussid_võrdlustatud = []
    
    for buss_1 in bussid:
        sobib = True
        for buss_2 in bussid:
            # kui mingil teisel bussil on väljumisaeg hiljem, saabumisaeg varasem ning hind on väiksem
            if buss_2[0] > buss_1[0] and buss_2[1] < buss_1[1] and int(buss_2[2]) < int(buss_1[2]):
                # siis jooksev buss (buss_1) juba ei sobi
                sobib = False
        if sobib:
            bussid_võrdlustatud.append(buss_1)
    
    return bussid_võrdlustatud
#############################################################################################
failinimi = input("Sisesta failinimi: ")
f = open(failinimi)
bussid = [rida.strip().split() for rida in f]
f.close()

bussid = järjesta(võrdle(bussid))
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for buss in bussid:
    print(buss[0], buss[1], buss[2])
#############################################################################################