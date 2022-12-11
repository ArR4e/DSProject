def erinevad_sümbolid(tekst):
    tekst = tekst.strip()
    nimekiri = set()
    for a in tekst:
        nimekiri.add(a)
        
    return nimekiri

def sümbolite_sagedus(tekst):
    uus = {}
    for a in tekst:
        if a not in uus:
            uus[a] = int(1)
        else:
            uus[a] = int(int(uus.get(a))+1)
    return uus

def grupeeri(tekst):
    taishaalik = 'aeiouõäöüAEIOUÕÄÖÜ'
    kaashaalik = 'bdfghjklmnprsšzžtvBDFGHJKLMNPRSŠZŽTV'
    muud = '!?.,#%&/()=[]{}+-_;: 1234567890'
    final = {
        'Täishäälikud' : {},
        'Kaashäälikud' : {},
        'Muud' : {},
        }
    n = sümbolite_sagedus(tekst)
    print(n)
    
    

    for a in n:
        if a in taishaalik:
            if final.get('Täishäälikud')!={}:
                kokku = set()
                eelnev = final('Täishäälikud')
                kokku.add(eelnev)
                kokku.add
                #summa = arv + n.get(a)
                final['Täishäälikud'] = kokku
            else:
                final['Täishäälikud'] = n.get(a)
            #print(a)
        if a in kaashaalik:
            if final.get('Kaashäälikud')!={}:
                arv = final.get('Kaashäälikud')
                summa = arv + n.get(a)
                final['Kaashäälikud'] = summa
            else:
                final['Kaashäälikud'] = n.get(a)
            #print(a)
        if a in muud:
            if final.get('Muud')!={}:
                arv = final.get('Muud')
                summa = arv + n.get(a)
                final['Muud'] = summa
            else:
                final['Muud'] = n.get(a)
            #print(a)
    print(final)
        
        
        
'''        
        if a[0] in taishaalik:
            #if final.get('Täishäälikud') is not None:
            print('taishaalik: '+a)
        if a[0] in kaashaalik:
            print('kaashaalik ' + a)
        
        if a[0] in muud:
            print('muu '+a)
        
        #print(a)
'''
        
        
print(erinevad_sümbolid('hulk ei sisalda'))
print(sümbolite_sagedus('Heihopsti!! tegelane::)'))
print(grupeeri('Sõida tadsa üle silla!!'))