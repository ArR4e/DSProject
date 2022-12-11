def erinevad_sümbolid(sõne):
    a = set()
    for i in sõne:
        a.add(i)
    return(a)

def sümbolite_sagedus(sõne):
    a = {}
    for i in sõne:
        if i in a:
            a[i] = a[i] + 1
        else:
            a[i] = 1
    return(a)

def grupeeri(sõne):
    a = sümbolite_sagedus(sõne)
    põhi = {'Täishäälikud': {}, 'Kaashäälikud': {}, 'Muud': {}}
    täis=[]
    kaas = []
    muu = []
    for i in a:
        if i.lower() in 'aeiouõäöü':
            täis.append((i,a[i]))
        elif i in 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy':
            kaas.append((i,a[i]))
        else:
            muu.append((i,a[i]))
    põhi['Täishäälikud']=set(täis)
    põhi['Kaashäälikud']=set(kaas)
    põhi['Muud']=set(muu)
    return(põhi)



    
    
    
    
    
    