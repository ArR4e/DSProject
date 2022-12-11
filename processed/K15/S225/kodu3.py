def kellaaegade_võrdlus(aeg1, aeg2):
    aeg1_tunnid, aeg1_minutid = aeg1.split(':')
    aeg2_tunnid, aeg2_minutid = aeg2.split(':')
    if aeg1_tunnid < aeg2_tunnid or (aeg1_tunnid == aeg2_tunnid and aeg1_minutid < aeg2_minutid):
        return True
    return False

def busside_võrdlus(buss1, muud_bussid):
    for buss2 in muud_bussid:
        if kellaaegade_võrdlus(buss1[0], buss2[0]) and not kellaaegade_võrdlus(buss1[1], buss2[1]) and float(buss1[2]) > float(buss2[2]):
            return False
    return True
    
plaan = input('Sisesta failinimi: ')


with open(plaan, encoding='utf-8') as sõiduplaan:
    bussiajad = []
    for rida in sõiduplaan:
        rida = rida.replace('\n','').split()
        bussiajad.append(rida)
    
sobivad_bussid = []
for bussi_indeks in range(len(bussiajad)):
    if busside_võrdlus(bussiajad[bussi_indeks], bussiajad):
        sobivad_bussid.append(bussiajad[bussi_indeks])
        
for bussi_indeks1 in range(len(sobivad_bussid) - 1):
    for bussi_indeks2 in range(bussi_indeks1 + 1, len(sobivad_bussid)):
        if sobivad_bussid[bussi_indeks1][0] > sobivad_bussid[bussi_indeks2][0]:
            sobivad_bussid[bussi_indeks1], sobivad_bussid[bussi_indeks2] = sobivad_bussid[bussi_indeks2], sobivad_bussid[bussi_indeks1]

print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
for buss in range(len(sobivad_bussid)):
    print(str(sobivad_bussid[buss][0]) +' ' + str(sobivad_bussid[buss][1]) + ' ' + str(sobivad_bussid[buss][2]))
