from matplotlib import pyplot

fail = open("aktsiad.txt")
aktsiad = []
for rida in fail: #eraldab failist ainult aktsiate hinnad
    rida = rida.strip("\n")
    rida = rida.split(",")
    rida = rida[1]
    aktsiad.append(float(rida))
fail.close()

def silu_andmed(aktsiad, n):
    silutud = []
    koht = 0
    järg = 1
    while True:
        summa = 0
        if koht >= len(aktsiad): #andmete lõppemisel, lõpeta tsükkel
            break
        
        elif koht < n: #kui andmeid vähem kui keskmistamisele ette antud
            for i in range(koht+1): #liidab kõik elemendid kuni etteantid elemendini kokku
                summa += aktsiad[i]
                keskmine = summa/(koht+1)
                silutud.append(keskmine)
                koht += 1
        else: #kui andmeid rohkem kui keskmistamisele antud
            for i in range(järg, koht+1): #liidab kõik elemendid etteantud vahemikus kokku
                summa += aktsiad[i]
            keskmine = summa/(n)
            silutud.append(keskmine)
            koht += 1
            järg += 1
    return silutud

silutud = silu_andmed(aktsiad, 50) #tagastatud andmetele antakse väärtus

joonis = pyplot.figure()
ala = joonis.add_subplot(1, 1, 1) #loob joonistamiseks koha
ala.plot(aktsiad) #joonistab algsed hinnad
ala.plot(silutud) #joonistab silutud hinnad
pyplot.show() #näitab joonist kasutajale