from statistics import harmonic_mean

def silu_andmed(andmed, n):
    keskmistatud_andmed = []
    for i in andmed:
        elemendid = []
        indeks = andmed.index(i)
        viimane_indeks = indeks - n
        while indeks >= viimane_indeks:
            elemendid.append(andmed[indeks])
            indeks -= 1
        uus_i = harmonic_mean(elemendid)
        keskmistatud_andmed += uus_i