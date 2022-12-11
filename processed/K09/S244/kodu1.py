from statistics import harmonic_mean


def silu_andmed(täisarv, järjend):
    uus_järjend = []
    ajutine_järjend = []
    k = len(järjend)
    for x in range(k):
        if x + 1 >= täisarv:
            for m in range(täisarv):
                ajutine_järjend.append(järjend[x-m])
            liige = harmonic_mean(ajutine_järjend)
            uus_järjend.insert(x, liige)
            ajutine_järjend = []
                
               
        if x + 1 < täisarv:
            for t in range(x+1):
                ajutine_järjend.append(järjend[x-t])
            liige = harmonic_mean(ajutine_järjend)
            uus_järjend.insert(x, liige)
            ajutine_järjend = []
            
    return uus_järjend
        
    
        
        
täisarv = int(input('Sisestage täisarv: '))
fail = open('aktsiad.txt')
järjend = []
for x in fail:
    x = x.strip()
    y = list(x.split(','))
    for x in y:
        try:
            x = float(x)
            järjend.append(x)
        except ValueError:
            pass
print(silu_andmed(täisarv, järjend))