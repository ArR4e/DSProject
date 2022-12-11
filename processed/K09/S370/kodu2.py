from random import randint

def minu_shuffle(j):
    r=len(j)-1
    for n in range(r*10):
        i=randint(0,r)
        k=randint(0,r)
        j[i], j[k] = j[k], j[i]
        
järjend=input("Siseta järjend, eralda elemendid komadega: ").split(",")
minu_shuffle(järjend)
print("Segatud järjend on", järjend)