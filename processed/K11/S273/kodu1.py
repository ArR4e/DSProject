flapsed = open("lapsed.txt", encoding="utf-8")
kellelaps = flapsed.readlines()
fnimed = open("nimed.txt", encoding="utf-8")
nimed = fnimed.readlines()
lapsedtxt = "lapsed.txt"
nimedtxt = "nimed.txt"

def seosta_lapsed_ja_vanemad(lapsed, Nimed):
    dictnimed = dict()
    for nimi in nimed:
        a = nimi.strip().split()
        dictnimed[a[0]] = a[1] + " " + a[2]

    dictkellelaps = dict()
    for element in kellelaps:
        a = element.strip().split()
        if a[1] not in dictkellelaps:
            dictkellelaps[a[1]] = a[0]
            continue
        if a[1] in dictkellelaps:
            dictkellelaps[a[1]] = [dictkellelaps[a[1]], a[0]]

    # for element in dictkellelaps:
    #     laps = dictnimed[element]
    #     vanemad = ""
    #     if type(dictkellelaps[element]) == str:
    #         vanemad += dictnimed[dictkellelaps[element]]
    #         print(laps + ": " + vanemad)
    #     if type(dictkellelaps[element]) == list:
    #         vanemad = dictnimed[dictkellelaps[element][0]] + ", " + dictnimed[dictkellelaps[element][1]]
    #         print(laps + ": " + vanemad)
    maindict = dict()
    for element in dictkellelaps:
        laps = dictnimed[element]
        vanemad = set()
        if type(dictkellelaps[element]) == str:
            vanemad.add(dictnimed[dictkellelaps[element]])
        if type(dictkellelaps[element]) == list:
            vanemad = {dictnimed[dictkellelaps[element][0]], dictnimed[dictkellelaps[element][1]]}
        maindict[laps] = vanemad
    return maindict

seosta_lapsed_ja_vanemad(lapsedtxt, nimedtxt)
print(seosta_lapsed_ja_vanemad(lapsedtxt, nimedtxt))