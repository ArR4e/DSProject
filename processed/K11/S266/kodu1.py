def loe_lapsed(laste_fail, nimed):
    with open('lapsed.txt', 'r', encoding = 'UTF-8') as f:
        andmed = f.read().split('\n')
    laste_vanemad = {}
    for rida in andmed:
        kirje = rida.split()
        if nimed[kirje[1]] not in laste_vanemad:
            laste_vanemad[nimed[kirje[1]]] = set()
        laste_vanemad[nimed[kirje[1]]].add(nimed[kirje[0]])
    return laste_vanemad

def loe_nimed(nimede_fail):
    with open('nimed.txt', 'r', encoding = 'UTF-8') as f:
        andmed = f.read().split('\n')
    nimed = {}
    for rida in andmed:
        kirje = rida.split(maxsplit = 1)
        nimed[kirje[0]] = kirje[1]
    return nimed

def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    nimed = loe_nimed(nimede_fail)
    lapsevanemad = loe_lapsed(laste_fail, nimed)
    return lapsevanemad

lapsevanemad = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

for laps, vanemad in lapsevanemad.items():
    print(laps + ': ' + ', '.join(vanemad))
