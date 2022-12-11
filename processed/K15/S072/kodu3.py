def tunnid_to_min(tunnid):
    splittitud = tunnid.split(':')
    
    tunnid = int(splittitud[0])
    minutid = int(splittitud[1])
    
    return tunnid * 60 + minutid

failinimi = input("Sisesta failinimi: ")

with open(failinimi, "r") as f:
    bussid = [x.strip().split(' ') for x in f.readlines()]

sobivad_bussid = []
for buss in bussid:
    bussi_väljumine = tunnid_to_min(buss[0])
    bussi_saabumine = tunnid_to_min(buss[1])
    esimese_hind = int(buss[2])
    
    sobib = True
    for teine_buss in bussid:
        teise_bussi_väljumine = tunnid_to_min(teine_buss[0])
        teise_bussi_saabumine = tunnid_to_min(teine_buss[1])
        
        teise_hind = int(teine_buss[2])
        
        if bussi_väljumine < teise_bussi_väljumine and bussi_saabumine > teise_bussi_saabumine and esimese_hind > teise_hind:
            sobib = False
            break
    if sobib:
        sobivad_bussid.append(buss)

for buss in sorted(sobivad_bussid, key=lambda x: x[0]):
    print(*buss)          
