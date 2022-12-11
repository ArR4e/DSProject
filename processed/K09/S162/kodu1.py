from statistics import harmonic_mean
def silu_andmed(järjend,arv):
    uusjärjend=[]
    n=0
    for el in järjend:
        muutuvjärjend=järjend[0:arv+1]
        uusjärjend.append(harmonic_mean(muutuvjärjend))
        järjend.pop(0)
    return uusjärjend
print(silu_andmed([2,1,3,4,5],3))
print(harmonic_mean([1]))