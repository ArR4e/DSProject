lapsed = open("lapsed.txt")
nimed = open("nimed.txt")

def seosta_lapsed_ja_vanemad(lapsed, nimed):
    sõnastik = {}
    isikukoodide_sõnastik = {}
    for rida in nimed:
        rida = rida.strip().split(" ",1)
        isikukoodide_sõnastik[rida[0]] = rida[1]
    for rida in lapsed:
        rida = rida.strip().split(" ")
        if isikukoodide_sõnastik[rida[1]] in sõnastik:
            sõnastik[isikukoodide_sõnastik[rida[1]]].add(isikukoodide_sõnastik[rida[0]])
        else:
            sõnastik[isikukoodide_sõnastik[rida[1]]] = set()
            sõnastik[isikukoodide_sõnastik[rida[1]]].add(isikukoodide_sõnastik[rida[0]])
    return sõnastik