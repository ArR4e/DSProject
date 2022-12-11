def seosta_lapsed_ja_vanemad(lapsed, nimed):
    s6nastik={}
    nimede_s = {}
    
    lapsed = open("lapsed.txt")
    for rida in lapsed:
        vanem, laps = rida.strip().split(" ")
        s6nastik.setdefault(laps, []).append(vanem)
        
    nimed = open("nimed.txt")
    for rida in nimed:
        kood, nimi = rida.strip().split(" ", 1)
        nimede_s[kood] = nimi
    if laps in nimede_s:
        True
    else:
        nimede_s[laps] = set()
                
    for laps in s6nastik:
        if len(s6nastik[laps]) == 2:
            print(nimede_s[laps] + ": " + str(nimede_s[s6nastik[laps][0]]) + "," + str(nimede_s[s6nastik[laps][1]]))
        else:
            print(nimede_s[laps] + ": " + str(nimede_s[s6nastik[laps][0]]))
    lapsed.close()
    nimed.close()
    return s6nastik
sõnastik = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')