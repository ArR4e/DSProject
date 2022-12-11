from matplotlib import pyplot
f = open("aktsiad.txt")
aktsiad = []
for rida in f:
    rida = rida.strip("\n")
    rida = rida.split(",")
    rida = rida[1]
    aktsiad.append(float(rida))
f.close()

def silu_andmed(aktsiad,n):
    silutud = []
    koht = 0
    järg = 1
    while True:
        summa = 0
        if koht >= len(aktsiad):
            break
        
        elif koht < n:
            for i in range(koht + 1):
                summa += aktsiad[i]
            keskmine = summa/(koht+1)
            silutud.append(keskmine)
            koht += 1
        else:
            for i in range(järg, koht+1):
                summa += aktsiad[i]
            keskmine = summa/(n)
            silutud.append(keskmine)
            koht += 1
            järg += 1
                
    return silutud
silutud = silu_andmed(aktsiad,50)

joonis = pyplot.figure()
ala = joonis.add_subplot(1,1,1)
ala.plot(aktsiad)
ala.plot(silutud)
pyplot.show()