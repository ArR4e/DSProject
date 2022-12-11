def seosta_lapsed_ja_vanemad(fail1, fail2):
    f1 = open(fail1, encoding="UTF-8")
    
    sõnastik = {}
    h = []
    
    for rida in f1:
        vanemlaps = rida.split()
        f2 = open(fail2, encoding="UTF-8")
        for el in f2:
            i = 0
            vahe1 = ""
            vahe2 = ""
            for elem in el:
                if i == 0 and elem != " ":
                    vahe1 += elem
                elif i == 0 and elem == " ":
                    i += 1
                else:
                    vahe2 += elem
            
            isiknimi = [vahe1, vahe2.strip()]
            
            if vanemlaps[0] == isiknimi[0]:
                vanemlaps[0] = isiknimi[1]
           
            if vanemlaps[1] == isiknimi[0]:
                vanemlaps[1] = isiknimi[1]
            
        h = [vanemlaps[1], vanemlaps[0]]
        if vanemlaps[1] not in sõnastik:
            sõnastik[vanemlaps[1]] = {vanemlaps[0]}
        else:
            väärtus = sõnastik.get(vanemlaps[1])
            väärtus.add(str(vanemlaps[0]))
            sõnastik[vanemlaps[1]] = väärtus
        
        f2.close()
    f1.close()
    
    return sõnastik

seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")