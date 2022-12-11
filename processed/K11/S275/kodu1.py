def seosta_lapsed_ja_vanemad(lapsed, vanemad):
    x = open(lapsed, encoding="UTF-8")
    y = open(vanemad, encoding="UTF-8")
    a = []
    b = []
    c = {}
    e = {}
    for rida in x:
        osad = rida.strip("\n").split()
        vanem = osad[0]
        laps = osad[1]
        
        a.append(laps)
        b.append(vanem)
        
    
    for rida2 in y:
        osad2 = rida2.split()
        isik = osad2[0]
        nimi = osad2[1] + " " + osad2[2]
        c[isik] = nimi
    
    for j in range(len(a)):
        index = [i for i, x in enumerate(a) if x == a[j]]
        d = []
        for el in range(len(index)):
            d.append(c[b[index[el]]])
        e[c[a[j]]] = set(d)
            
    return e


#Uninstallisin eile Thonny, kuna projektiga tegeledes läks see katki ja unustasin Logide salvestamise sisse lülitada :((sss