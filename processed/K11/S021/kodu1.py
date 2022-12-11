def seosta_lapsed_ja_vanemad(lapsed, nimed):
    lastefail = open(lapsed, encoding = "UTF-8")
    nimedefail = open(nimed, encoding = "UTF-8")
    
    tulemussõnastik = {}
    sõnastik = {}
    for nimirida in nimedefail:
        nimedejärjend = nimirida.strip().split(" ")
        sõnastik[nimedejärjend[0]] = nimedejärjend[1] + " " + nimedejärjend[2]
        
    for isikukoodid in lastefail:
        isikutejärjend = isikukoodid.strip().split(" ")
        vanem = sõnastik[isikutejärjend[0]]
        laps = sõnastik[isikutejärjend[1]]
        
        if laps in tulemussõnastik:
            tulemussõnastik[laps].add(vanem)
        else:
            tulemussõnastik[laps] = set()
            tulemussõnastik[laps].add(vanem)
            
    return tulemussõnastik
            
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")