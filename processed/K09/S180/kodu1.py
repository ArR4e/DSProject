import matplotlib.pyplot as plt

def silu_andmed(järjend, n):
    keskmistatud = []
    i = 1
    visatud = 0
    pikkus = 0
    jagatud = [1 / x for x in järjend]
    lisatud = 1
    
    while pikkus < len(järjend):
        if i >= n:
            i = n
            
        if visatud >= n:
            keskmistatud.append(str(i / sum(jagatud[n + lisatud - visatud:n + lisatud])))
            lisatud += 1
        else:
            keskmistatud.append(str(i / sum(jagatud[0:visatud + 1])))
            visatud += 1
        
        i += 1
        pikkus += 1
        
    return [float(numbrid) for numbrid in keskmistatud]

f = open(input('Faili nimi: '))

hinnad = []
päevad = []
p = 0

for rida in f:
    hinnad.append(rida.strip('\n').split(',')[1])
    p += 1
    päevad.append(p)

hinnad = ([float(hind_eraldi) for hind_eraldi in hinnad])

s = silu_andmed(hinnad, 50)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(päevad, hinnad, s)
ax.set_xlabel('päevad')
ax.set_ylabel('hind')

plt.show()