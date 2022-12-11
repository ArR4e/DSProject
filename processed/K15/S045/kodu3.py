def aeg(buss): #minutites
    buss_algus = buss[0].split(':')
    buss_lõpp = buss[1].split(':')
    return ((int(buss_lõpp[0]) * 60 + int(buss_lõpp[1])) - (int(buss_algus[0]) * 60 + int(buss_algus[1])))

def eemalda_halvad(bussid):
    vähim_aeg = None
    parim_hind = None
    for buss in bussid:
        sõidu_aeg = aeg(buss)
        if vähim_aeg == None:
            vähim_aeg = sõidu_aeg
        elif vähim_aeg > sõidu_aeg:
            vähim_aeg = sõidu_aeg
        
        sõidu_hind = float(buss[2]) * sõidu_aeg
        if parim_hind == None:
            parim_hind = sõidu_hind
        elif parim_hind > sõidu_hind:
            parim_hind = sõidu_hind
    
    head_bussid = list()
    for buss in bussid:
        sõidu_aeg = aeg(buss)
        if sõidu_aeg == vähim_aeg:
            head_bussid.append(buss)
        elif sõidu_aeg * float(buss[2]) == parim_hind:
            head_bussid.append(buss)
        
    
    return head_bussid
        

def leia_bussid(andmed):
    u_andmed = list() #uued andmed
    for rida in andmed:
        buss = rida.split(' ')
        u_andmed.append(buss)

    u_andmed.sort()
    bus_list = eemalda_halvad(u_andmed)
    return bus_list
        
def list_to_string(s): #https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    string = " "
    return string.join(s)

failinimi = input('Siseta failinimi: ')
with open(failinimi, 'r') as f:
    data = [x.strip() for x in f.readlines()]

bussid = leia_bussid(data)
print('Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:')
for buss in bussid:
    print(list_to_string(buss))
