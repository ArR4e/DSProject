import string
def erinevad_sümbolid(sõne):
    tähed = (string.printable + "öäõü")
    olemas = set()
    for täht in sõne:
        if täht.lower() in tähed:
            if täht.lower() not in olemas:
                olemas.add(täht)
    return(olemas)
print(erinevad_sümbolid("tere maa!lm"))



def sümbolite_sagedus(sõne):
    sagedus = {}
    for el in sõne:
        if el in sagedus:
            sagedus[el] = sagedus[el] +1
        else:
            sagedus[el] = 1
    return sagedus
print(sümbolite_sagedus("tere maLa !ilm?"))



def grupeeri(sõne):
    #loon tähtede jaoks tühjadhulgad
    täis = set()
    kaas = set()
    muu = set()
    sõnastik = {"Täishäälikud": täis, "Kaashäälikud": kaas, "Muud": muu}
    sõnastik1 = {}
    
    for sümbol in sõne:
        if sümbol in sõnastik1:
            sõnastik1[sümbol] += 1
        else:
            sõnastik1[sümbol] = 1
            
    for võti in sõnastik1.keys():
        tähepaar = (võti, sõnastik1[võti])
        
        if võti.lower() in ['a', 'e', 'i', 'o', 'u', 'ö','ä','õ','ü']:
            täis.add(tähepaar)
        elif võti.lower() in ['c','l', 'm', 'n','r','s','v','h','j','p','b','t','d','k','g','f','š','z','ž','y','x','w','q']:
            kaas.add(tähepaar)
        else:
            muu.add(tähepaar)
    return sõnastik
#print(grupeeri("tere maailm!"))


            
        
    

