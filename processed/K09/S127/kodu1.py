from statistics import harmonic_mean
f=open(input("Sisesta faili nimi: "))
järjend=[]
for rida in f:
    jupid=rida.split(",")
    hind=jupid[1]
    järjend=järjend+[hind]
f.close()
def silu_andmed(järjend, n):
    keskmine_hind=harmonic_mean(järjend)
    return silutud_järjend
vastus=silu_andmed(järjend, n)
print(vastus)