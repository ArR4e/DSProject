nimed=[]

def väljasta_liin(eellane,järglane,sõnastik):
    uus={}
    for x,y in sõnastik.items():
        for vanem in y:
            lapsed=uus.get(vanem,[])
            lapsed.append(x)
            uus[vanem]=lapsed
            
    for x,y in sõnastik.items():
        if eellane in y and len(uus[eellane])==1:
            nimed.append(eellane)
            
            if järglane==x:
                nimed.append(järglane)
                for nimi in nimed:
                    print(nimi)
                return True
            
            else:
                return väljasta_liin(x,järglane,sõnastik)
        
        elif eellane in y:
            for laps in uus[eellane]:
                if laps!=järglane:
                    del sõnastik[laps]
            
            return väljasta_liin(eellane,järglane,sõnastik)         
    return False
