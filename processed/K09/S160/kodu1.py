from statistics import harmonic_mean
import matplotlib.pyplot as plt

andmed_aktsia = open(input("Sisestage uuritav fail: "))

n = 50
jarjend = []
jarjend2 = jarjend

for data in andmed_aktsia: 
    hind = data.split(' ')
    hind = hind[-1]
    hind = hind.split('\n')
    hind = hind[0]
    hind = float(hind)
    hind = jarjend.append(hind)

### MUUTMATA GRAAFIKU ARVUTUS
for indeks in range(1, len(jarjend) + 1):
     algus = max (0, indeks - n)
     (jarjend[algus:indeks])
   
### MUUDETUD GRAAFIKU ARVUTUS

for indeks in range(1, len(jarjend2) + 1):
    calculus =(0, n/(1/indeks))
    (jarjend[calculus:indeks])
    
### GRAAFIK I
muutmata = jarjend
plt.plot(muutmata)
print(muutmata)

### GRAAFIK II
#muudetud = newline
#plt.plot(muudetud)
#print(muudetud)

# KUVA
plt.show()

andmed_aktsia.close()