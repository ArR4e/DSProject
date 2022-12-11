sõne = input('Sisestage sõne: ')
hulk = {}
täishäälikud = "aeiouõäöü"
kaashäälikud = "hjlmrsvkpt"
sümbolid = "-' '"

def erinevaid_sümbolid(sõne):
    tähed = set(rida.strip() for rida in sõne)
    print(tähed)
 
      
def sümbolite_sagedus(sõne):
    for i in sõne:
        if i in hulk:
            hulk[i] += 1
        else:
            hulk[i] = 1
    print('Sagedus on:\n' + str(hulk))
    
def grupeeri(sõne, täishäälikud, kaashäälikud, sümbolid):
    sõne.casefold()
    loeng = {}.fromkeys(täishäälikud, 0)
    loeng2 = {}.fromkeys(kaashäälikud, 0)
    loeng3 = {}.fromkeys(sümbolid, 0)
    
    for char in sõne:
        if char in loeng:
            loeng[char] += 1
    print("Täishäälikud: ", loeng)
    
    for a in sõne:
        if a in loeng2:
            loeng2[a] += 1
    print("Kaashäälikud: ", loeng2)
    
    for b in sõne:
        if b in loeng3:
            loeng3[b] += 1      
    print("Sümbolid: ", loeng3)

    
erinevaid_sümbolid(sõne)
sümbolite_sagedus(sõne)
grupeeri(sõne, täishäälikud, kaashäälikud, sümbolid)

    

    
    