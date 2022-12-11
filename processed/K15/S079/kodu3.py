# 3. Bussid
# Tekstifailis on kirjas busside sõiduplaan kahe linna vahel.
# Igas reas on tühikutega eraldatult kirjas bussi väljumisaeg vormingus hh:mm, bussi saabumisaeg samas vormingus ja sõidu hind eurodes.

# Ilmselt ei tasu esimesest linnast teise sõitmiseks valida bussi,
#  - mille väljumisaeg on varasem,
# - saabumisaeg hilisem
# - ja sõidu hind suurem kui mõnel teisel bussil.
# Kirjuta programm, mis küsib kasutajalt failinime, loeb sellest failist sisse busside sõiduplaani ning väljastab ekraanile
# väljumisaegade järjestuses kõik bussid, mis kõigi niisuguse omadusega busside eemaldamisel alles jäävad.

# Näiteks kui sõiduplaanide faili sisu on

# 09:00 11:30 5
# 10:00 13:00 6
# 09:15 12:15 7
# 09:30 12:00 6
# 10:15 12:45 5
# siis peaks programm väljastama järgmise info:

# Sisesta failinimi: sõiduplaan.txt
# Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:
# 09:00 11:30 5
# 09:30 12:00 6
# 10:15 12:45 5

#failinimi = "bussid.txt"

failinimi = input("Sisesta failinimi: ")

# Lahenduse algoritm (kui fail sisse loetud):
# 1. sordi bussid (1) väljumisaja, (2) hinna, (3) saabumisaja järgi

f = open(failinimi)

bussid = []
for rida in f:
    rida = rida.strip().split()
    bussid.append(rida)
f.close()


bussid.sort(reverse = True)


bussid2 = []

for buss in bussid:
    sobib = True
    for buss2 in bussid:
        if (buss[0] < buss2[0]) and (buss[2] > buss2[2]) and (buss[1] > buss2[1]):
            sobib = False
    bussid2.append(sobib)
    
for i in range(len(bussid2)):
    if bussid2[i] == False:
        del bussid[i]
       # print(f'{bussid[i][0]} {bussid[i][1]} {bussid[i][2]}')
    else:
        pass

bussid3 = []
for buss in bussid:
    sobib = True
    for buss2 in bussid:
        if (buss[0] < buss2[0]) and (buss[2] > buss2[2]) and (buss[1] > buss2[1]):
            sobib = False
    bussid3.append(sobib)
    
for i in range(len(bussid3)):
    if bussid3[i] == False:
        del bussid[i]
       # print(f'{bussid[i][0]} {bussid[i][1]} {bussid[i][2]}')
    else:
        pass

bussid.sort()

    
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
    
for i in range(len(bussid)):
       print(f'{bussid[i][0]} {bussid[i][1]} {bussid[i][2]}')




