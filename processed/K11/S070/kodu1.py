
VANEMATE_KOODID = []
LASTE_KOODID = []
INFO = {}

def seosta_lapsed_ja_vanemad(lapsed, nimed):
    
    def tuvasta_nimi(kood):
        kood = int(kood)
        with open(nimed, "r", encoding="UTF8") as g:
            for rida in g:
                rida = rida.strip()
                g_info = rida.split(" ",1)
                if int(g_info[0]) != kood:
                    continue
                else:
                    nimi = g_info[1]
                    return nimi
    
    
    with open(lapsed, "r", encoding="UTF8") as f:
        #loeb sisse lapsed + vanemad + info
        for f_rida in f:
            f_rida = f_rida.strip()
            f_info = f_rida.split(" ") 
            f_vanem = f_info[0]
            f_laps = f_info[1]
            
            laps = tuvasta_nimi(f_laps)
            vanem = tuvasta_nimi(f_vanem)
            
            if laps not in INFO:
                INFO[laps] = set()
            INFO[laps].add(vanem)
            if f_laps not in LASTE_KOODID:
                LASTE_KOODID.append(laps)
            if f_vanem not in VANEMATE_KOODID:
                VANEMATE_KOODID.append(vanem)

    return INFO
    
print(seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt"))
        
        