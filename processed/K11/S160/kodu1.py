f1 = open("lapsed.txt")
f2 = open("nimed.txt")

def seosta_lapsed_ja_vanemad(fail1,fail2):
    lapsed = []
    nimed = []
    kids = []
    sonastik = {}
    family = []
    for rida in fail1:
        rida = fail1.readline()
        rida = rida.strip("\n")
        rida = rida.split(" ")
        lapsed.append(rida)
    for row in fail2:
        row = fail2.readline()
        row = row.strip('\n')
        row = row.split(' ')
        nimed.append(row)
    for x in lapsed :
        for y in nimed :
            if x[0] == y[0]:
                family.append(y[-2:])
            if x[1] == y[0]:
                kids.append(y[-2:])
                
    return sonastik

seosta_lapsed_ja_vanemad(f1,f2)