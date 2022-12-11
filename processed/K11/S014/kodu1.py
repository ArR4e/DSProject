# Põhitöö tuleks delegeerida funktsioonile seosta_lapsed_ja_vanemad,
# mille parameetriteks on laste faili nimi ja nimede faili nimi ning mis tagastab sõnastiku,
# kus kirje võtmeks on lapse nimi ja väärtuseks tema vanemate nimede hulk.

isikukoodid=open('lapsed.txt')
vanemad=open('nimed.txt')

def seosta_lapsed_ja_vanemad(isikukoodid,vanemad):
    sõnastik={}
    
    for rida in isikukoodid:
        if rida=='':
            break
        andmed=rida.strip().split()
        for kood in andmed:
            sõnastik[andmed[0]]=andmed[1]
        
    print(sõnastik)
    return sõnastik

seosta_lapsed_ja_vanemad(isikukoodid, vanemad)

isikukoodid.close()
vanemad.close()

    