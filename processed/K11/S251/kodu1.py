def seosta_lapsed_ja_vanemad(lapsed,nimed):
    laste_fail = open(lapsed,"r",encoding="utf-8")
    nimede_fail = open(nimed,"r",encoding="utf-8")
    
    lapsed = []
    vanemad = []
    sõnastik = {}
    
    while True:
        rida = laste_fail.readline()
        if rida == "":
            break
        rida = rida.strip("\n")
        andmed = rida.split(" ")
        
        vanemad.append(andmed[0])
        lapsed.append(andmed[1])
    
    kood_nimeks = nimede_fail.readlines()
    
    for i in range(len(lapsed)):
        
        for j in kood_nimeks:
            
            if lapsed[i] in j:
                laps = j[12:].strip("\n")
            if vanemad[i] in j:
                vanem = j[12:].strip("\n")
        if laps in sõnastik:
            sõnastik[laps].add(vanem)
        else:
            sõnastik[laps] = {vanem}
                            
    return sõnastik
        

sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt")

vanemad = ""
for i in sõnastik:
    for j in sõnastik[i]:
        vanemad += j + ", "
    vanemad = vanemad[:-2]

    print (i + ": " + vanemad)
    vanemad = ""