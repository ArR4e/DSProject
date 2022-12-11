from statistics import harmonic_mean
import matplotlib.pyplot as plt

algandmed=open('aktsiad.txt')
kuu=[]
kuupäev=[]
aasta=[]
kole_arv=[]
ilus_arv=[]

for andmed in algandmed:
    if andmed=='':
        break
    else:
        andmed=andmed.split()
        kuu.append(andmed[0])
        kuupäev.append(andmed[1])
        aasta.append(andmed[2])
        kole_arv.append(andmed[3])



def silu_andmed(kole_arv,mitmekaupa):
    ilus_arv=[]
    for arv in range(0,len(kole_arv),mitmekaupa):
        kole_arv[arv:arv+mitmekaupa]
        ilus_arv.append(harmonic_mean(kole_arv))
    return ilus_arv

print(silu_andmed([2, 1, 3, 4, 5], 3))

    
#     while the_list:
#         result_list.append(the_list[:chunk_size])
#         the_list = the_list[chunk_size:]
#     return result_list



algandmed.close()