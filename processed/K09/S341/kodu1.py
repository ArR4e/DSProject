import matplotlib
from statistics import harmonic_mean
andmed = []
täisarv=[]
with open('aktsiad.txt', encoding = 'UTF-8') as f1:
    for rida in f1:
        nimi= rida.split()[3]
        andmed.append(nimi)
    def silu_andmed(andmed,täisarv):
        täisarv = len(andmed)
        
        n = 0
        while n < täisarv:
            n += 1
        return n/(harmonic_mean(andmed))
            
print(silu_andmed(andmed,täisarv))