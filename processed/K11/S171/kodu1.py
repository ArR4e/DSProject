def seosta_lapsed_ja_vanemad(faillapsed, failnimed):
    seosednimed = {}
    seosedvanemad = {}
    with open(failnimed) as f:
        for rida in f:
            andmed = rida.strip().split(' ', 1)
            seosednimed[andmed[0]] = andmed[1]
    with open(faillapsed) as f:
        for rida in f:
            koodid = rida.strip().split()
            if seosednimed[koodid[1]] not in seosedvanemad:
                seosedvanemad[seosednimed[koodid[1]]] = {seosednimed[koodid[0]]}
            else:
                seosedvanemad[seosednimed[koodid[1]]].add(seosednimed[koodid[0]])
    return seosedvanemad


nimekiri = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for laps, vanemad in nimekiri.items():
    if len(vanemad) == 1:
        print(f'{laps}: {vanemad.pop()}')
    else:
        print(f'{laps}: {vanemad.pop()}, {vanemad.pop()}')
