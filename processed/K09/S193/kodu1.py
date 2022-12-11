# fail = open("aktsiad.txt" , "r")

from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(aktsia_h_keskmistamine, n):
    uus_keskmistatud_andmed = []
    a = []
    järjend = aktsia_h_keskmistamine[:]
    for i in aktsia_h_keskmistamine:
        a.append(järjend.pop)
        if len(a) > n:
            a.pop(0)
    
a = input("Sisestage faili nimi: ")
fail = open(a, "r")
for rida in fail:
    
    
fail.close




            
        
        