f = open(input("Sisesta failinimi: "))

def on_varasem(a, b):
    a_tunnid, a_minutid = a.split(':')
    b_tunnid, b_minutid = b.split(':')
    if int(a_tunnid) < int(b_tunnid):
        return True
    elif int(a_tunnid) == int(b_tunnid) and int(a_minutid) < int(b_minutid):
        return True
    else:
        return False
    
def parem(buss, teised_bussid):
    for buss2 in teised_bussid:
        if on_varasem(buss[0], buss2[0]) and not on_varasem(buss[1], buss2[1]) and int(buss[2]) > int(buss2[2]):
            return False
    else:
        return True
    
bussid = []
sobivad_bussid = []
for rida in f: #kirjutame faili read järjendisse
    bussid.append(rida.split())
    #[0] - väljumisaeg
    #[1] - saabumisaeg
    #[2] - hind
    
for i in range(len(bussid)):
    if parem(bussid[i], bussid):
        sobivad_bussid.append(bussid[i])
        
for i in range(len(sobivad_bussid)-1):
    for j in range(i+1, len(sobivad_bussid)):
        if sobivad_bussid[i][0] > sobivad_bussid[j][0]:
            sobivad_bussid[i], sobivad_bussid[j] = sobivad_bussid[j], sobivad_bussid[i]

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for buss in sobivad_bussid:
    print(" ".join(buss))
    
    
    