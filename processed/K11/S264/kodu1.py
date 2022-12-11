lapsed = open('lapsed.txt', encoding = 'utf-8')
nimed = open('nimed.txt', encoding = 'utf-8')

def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    s = {}
    isikukoodid = {}
    nimed_ik = {}
    for rida in lastefailinimi:
        if rida != '\n':
            andmed = rida.strip().split()
            isikukoodid[andmed[1]] = andmed[0]
    for rida in nimedefailinimi:
        if rida != '\n':
            nimedega = rida.strip().split(' ', 1)
            nimed_ik[nimedega[0]] = nimedega[1]
            if nimedega[0] in isikukoodid.keys():
                s[nimedega[1]] = set()
    for lapse, vanema in isikukoodid.items():
        laps = nimed_ik[lapse]
        vanem = nimed_ik[vanema]
        s[laps].add(vanem)
    return s

print(seosta_lapsed_ja_vanemad(lapsed, nimed))

lapsed.close()
nimed.close()