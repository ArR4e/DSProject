'''-- Kodutöö nr. 11 - 1. Lapsed ja vanemad --'''
'''Kirjuta programm, mis väljastab ekraanile iga lapse kohta ühe rea: nimi, koolon, tühik ning
   seejärel koma ja tühikuga eraldatuna ema ja isa nimi. Kui teada on ainult üks vanem, siis
   väljastada ainult see.'''
###################################################################################################
# funktsioon 'lapse_vanemad' loeb andmed failist 'laste_fail' sõnastikku 'lapsed'
# saadud sõnastik sisaldab võtmeteks laste isikukoodid ja väärtusteks laste vanemate isikukoodide hulka
def lapse_vanemad(laste_fail):
    f = open(laste_fail)
    lapsed = {}
    
    for rida in f:
        andmed = rida.strip().split()
        lapse_id = andmed[1]
        vanema_id = andmed[0]
        
        if lapse_id not in lapsed:
            lapsed[lapse_id] = set()
        lapsed[lapse_id].add(vanema_id)    
    
    f.close()
    return lapsed
###################################################################################################
# funktsioon 'id_nimed' loeb andmed failist 'nimede_fail' sõnastikku 'nimed'
# saadud sõnastik sisaldab võtmeteks isikukoodid ja väärtusteks inimese täisnimi sõnena
def id_nimed(nimede_fail):
    f = open(nimede_fail, encoding = 'utf-8')
    nimed = {}
    
    for rida in f:
        andmed = rida.strip().split()
        nimed[andmed[0]] = ' '.join(andmed[1:])
    
    f.close()
    return nimed
###################################################################################################
# funktsiooni 'seosta_lapsed_ja_vanemad' parameetriteks on laste faili nimi ja nimede faili nimi
# tagastab sõnastiku, kus kirje võtmeks on lapse nimi ja väärtuseks tema vanemate nimede hulk
def seosta_lapsed_ja_vanemad(laste_fail, nimede_fail):
    # leida iga lapse vanemate isikukoodid vormingus {'lapse id': {vanem id, vanem id}}
    lapsed = lapse_vanemad(laste_fail)
    # leida iga isikukoodi järgi inimese täisnimi vormingus {'id': 'täisnimi'}
    nimed = id_nimed(nimede_fail)
    
    # leida iga lapse nimi ja tema vanemate nimed isikukoodide järgi 
    # salvestada uude sõnastikku 'lapsed_vanemad'
    lapsed_vanemad = {}
    
    for lapse_id in lapsed:
        vanemad = set()
        for vanema_id in lapsed[lapse_id]:
            vanemad.add(nimed[vanema_id])
        lapsed_vanemad[nimed[lapse_id]] = vanemad
    
    return lapsed_vanemad    
###################################################################################################
lapsed_vanemad = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
for laps in lapsed_vanemad:
    print(laps, end = ': ')
    print(', '.join(lapsed_vanemad[laps]))