def seosta_lapsed_ja_vanemad(laps="lapsed.txt",nim="nimed.txt"):
    f1=open(laps)
    f2=open(nim)
    laps_van={}
    lõpp={}
    for line in f1:
        line=line.strip().split()
        if line[1] in laps_van:
            laps_van[line[1]].add(line[0])
        else:
            laps_van[line[1]] = set()
            laps_van[line[1]].add(line[0])
    nem_lib={}
    for line in f2:
        line=line.strip().split()
        nimi=""
        for x in line[1::]:
            nimi += x+" "
        nem_lib[line[0]]=nimi.strip()
    for laps in laps_van:
        van=set()
        for x in laps_van[laps]:
            van.add(nem_lib[x])
        lõpp[nem_lib[laps]]=van
    f1.close()
    f2.close()
    return lõpp
m = seosta_lapsed_ja_vanemad()
for laps in m:
    vanemad=""
    for vanem in m[laps]:
        vanemad+=" "+vanem+","
    print(laps+":"+vanemad[0:-1])