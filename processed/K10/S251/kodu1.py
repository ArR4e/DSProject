def erinevad_sümbolid(sõne):
    hulk = set()
    for i in sõne:
        hulk.add(i)
    return hulk

def sümbolite_sagedus(sõne):
    sõnastik = {}
    for i in sõne:
        if i in sõnastik:
            sõnastik[i] += 1
        else:
            sõnastik[i] = 1
    return sõnastik

def grupeeri(sõne):
    täishäälikud = "AaEeIiOoUuÕõÄäÖöÜü"
    kaashäälikud = "QqWwRrTtYyPpSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm"
    
    täishääliku_hulk = set()
    kaashääliku_hulk = set()
    muu_hulk = set()
        
    baassõnastik = sümbolite_sagedus(sõne)
    
    for i in baassõnastik:
        
        if i in täishäälikud:
            täishääliku_hulk.add((i,baassõnastik[i]))
            
        elif i in kaashäälikud:
            kaashääliku_hulk.add((i,baassõnastik[i]))
            
        else:
            muu_hulk.add((i,baassõnastik[i]))
            
    lõppsõnastik = {"Täishäälikud" : täishääliku_hulk, "Kaashäälikud" : kaashääliku_hulk, "Muud" : muu_hulk}
    return lõppsõnastik
    

#lause = "hulk ei sisalda kunagi korduvaid elemente"
#hulk = erinevad_sümbolid("hulk ei sisalda kunagi korduvaid elemente")
#sõnastik = sümbolite_sagedus(lause)
#erinevad_häälikud = grupeeri("sõida tasa üle silla")
#print(erinevad_häälikud)
