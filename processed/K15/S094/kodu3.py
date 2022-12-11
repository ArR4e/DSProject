
def bussid(failinimi):
    fail = open(failinimi)
    for rida in fail:
        väljumine, saabumine, hind = rida.strip().split()
        väljumine_koolonita = väljumine.replace(':', '')
        saabumine_koolonita = saabumine.replace(':', '')
        väljumine_koolonita = int(väljumine_koolonita)
        saabumine_koolonita = int(saabumine_koolonita)
        hind = int(hind)
        
        if saabumine_koolonita - väljumine_koolonita <= 270:
            if hind <= 6:
                print(väljumine, saabumine, hind)                
    fail.close()
    return 0

failinimi = input('Sisesta failinimi: ')
bussid(failinimi)