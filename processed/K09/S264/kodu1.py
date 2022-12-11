#tekstifailis aktsiad.txt on igal real kuupäev+1 ettevõtte aktsia hind
#def silu_andmed(algandmed järjendina, int(mitme el kaupa kesmist.)):
    #rakendab aktsiate hindaldele keskmistamist
        #(iga järjendi el asenamine eelmise n elemendi harmoonilise
        #keskmisega)
    #tagastab keskmistatud andmed uue järjendina
from statistics import harmonic_mean
f = open('aktsiad.txt')
aktsia_hind = []
kuupäevad = []
for rida in f:
        kuupäevad.append(rida)
        i = int(f.readline().strip("\n"))
        aktsia_hind.append(i)
print(aktsia_hind)

def silu_andmed(aktsia_hind, n):
    for j in range(0, len(aktsia_hind)):
        while j == 0:
            keskmine = (sum(aktsia_hind[j:(n)]))/n
        if j <= (n-1):
            continue
        else:
            keskmine = (keskmine + aktsia_hind[j])/(j + 1)
        return keskmine

silu_andmed(aktsia_hind, 3)
