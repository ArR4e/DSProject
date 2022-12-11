#Kodutöö: 1. Lapsed ja vanemad

#f1 "lapsed.txt" -- vanema_isikukood lapse_isikukood
#f2 "nimed.txt" -- isikukood eesnimi perenimi

def seosta_lapsed_ja_vanemad(lapsed, nimed):
    sõnastik = {}
    l = []
    with open(lapsed) as f1:
        for rida in f1:
            rida.split()
            
    with open(nimed) as f2:
        for rida in f2:
            rida.split(" ", 2)

#vägagi poolik