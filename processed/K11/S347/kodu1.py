lastefailinimi = open("lapsed.txt")
nimedefailinimi = open("nimed.txt", encoding="utf-8")
def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    lastefailinimi = open("lapsed.txt")
    nimedefailinimi = open("nimed.txt", encoding="utf-8")
    sõnastik = {}
    lisasõnastik ={}
    lisasõnastik2 ={}
    lisasõnastik3 ={}
    järjend = []
    järjend2 = []
    järjend3 = []
    for rida in nimedefailinimi:
        järjend = rida.strip().split(" ", 1)
        nimi = järjend[1]
        isikukood = järjend[0]
        lisasõnastik[isikukood]= nimi

    for rida in lastefailinimi:
        järjend2= rida.strip().split()
        vanem = järjend2[0]
        laps= järjend2[1]
        if laps not in lisasõnastik2:
            lisasõnastik2[laps] = vanem
        if laps in lisasõnastik2:
            lisasõnastik3[laps] = vanem
                   
    for laps, vanem in lisasõnastik2.items():
        lapsenimi =lisasõnastik[laps]
        vanemanimi = lisasõnastik[vanem]
        if lapsenimi not in sõnastik:
            sõnastik[lapsenimi] = set()
            sõnastik[lapsenimi].add(vanemanimi)
        if lapsenimi in sõnastik:
            sõnastik[lapsenimi].add(vanemanimi)
    for laps, vanem in lisasõnastik3.items():
        lapsenimi =lisasõnastik[laps]
        vanemanimi = lisasõnastik[vanem]
        if lapsenimi not in sõnastik:
            sõnastik[lapsenimi] = set()
            sõnastik[lapsenimi].add(vanemanimi)
        if lapsenimi in sõnastik:
            sõnastik[lapsenimi].add(vanemanimi)
    return sõnastik

sõnastik = seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi)
for võti in sõnastik:
    if len(sõnastik[võti]) == 2:
        a = sõnastik[võti].pop()+", "+sõnastik[võti].pop()
        print(f"{võti}: {a}")
    if len(sõnastik[võti]) == 1:
        a = sõnastik[võti].pop()
        print(f"{võti}: {a}")


    
lastefailinimi.close()
nimedefailinimi.close()