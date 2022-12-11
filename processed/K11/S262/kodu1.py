#Kohalikus arvutis töötab, automaatkontrollis mitte?

def seosta_lapsed_ja_vanemad(lastefail,nimedefail):
    inimesed = {}
    lapsedjavanemad = {}
    for rida in nimedefail:
        andmed = rida.strip().split()
        inimesed[andmed[0]] = ' '.join(andmed[1:])
    for rida in lastefail:
        andmed = rida.strip().split()
        if inimesed[andmed[1]] in lapsedjavanemad:
            lapsedjavanemad[inimesed[andmed[1]]].add(inimesed[andmed[0]])
        else:
            a = set()
            a.add(inimesed[andmed[0]])
            lapsedjavanemad[inimesed[andmed[1]]] = a
    return lapsedjavanemad
nimed = open("nimed.txt",encoding="UTF-8")
lapsed = open("lapsed.txt",encoding="UTF-8")
