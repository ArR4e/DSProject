f1 = "lapsed.txt"
f2 = "nimed.txt"

def seosta_lapsed_ja_vanemad(f1,f2):
    fail1 = open(f1, "r", encoding="UTF-8")
    fail2 = open(f2, "r", encoding="UTF-8")
    
    lasteIDlist = []
    vanemateIDlist = []
    s = dict()
    while True:
        line = fail1.readline()
        if line == "":
            break
        line = line.strip().split(" ")
        vanemateIDlist.append(line[0])
        lasteIDlist.append(line[1])
        
    d = fail2.readlines()
    fail1.close()
    fail2.close()
    for i in range(len(lasteIDlist)):
        for j in d:
            if lasteIDlist[i] in j:
                laps = j[12:].strip()
            if vanemateIDlist[i] in j:
                vanem = j[12:].strip()
                
        if laps in s:
            s[laps].add(vanem)
        else:
            s[laps] = {vanem}
            
    return s

s = seosta_lapsed_ja_vanemad(f1,f2)
vanematesõne = ""
for k in s:
    for l in s[k]:
        vanematesõne += l
        
        print(str(k) + ": " + str(vanematesõne))
        vanematesõne = ""
    