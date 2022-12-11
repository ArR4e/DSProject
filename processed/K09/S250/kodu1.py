from statistics import harmonic_mean
import matplotlib.pyplot as plt
import copy

andmed_j = []
uued_andmed = []
lõpp_andmed = []

def silu_andmed(algandmed,el_arv):
    fail = open(algandmed, 'r', encoding='UTF-8')
    n = 0
    while True:
        rida = fail.readline()
        if rida == '':
            break
        else:
            n += 1
            andmed_j.append(abs(float(rida.split(',')[1].strip())))
            if n < el_arv:
                uued_andmed.append(harmonic_mean(andmed_j))
                lõpp_andmed.append(rida.split(',')[0].strip())
                lõpp_andmed.append(uued_andmed[n-1])
            if n >= el_arv:
                uued_andmed.append(harmonic_mean(andmed_j[n-el_arv:n+1]))
                lõpp_andmed.append(rida.split(',')[0].strip())
                lõpp_andmed.append(uued_andmed[n-1])
    return lõpp_andmed
    fail.close()
    
print(silu_andmed('aktsiad.txt',5))

