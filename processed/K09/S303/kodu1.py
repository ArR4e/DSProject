import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(jarjend, el_arv):
    harm_jarjend = []
    
    for i in range(len(jarjend)):
        temp_jarjend = []
        for j in range(0, el_arv):
            if i - j < 0: break
            temp_jarjend.append(jarjend[i-j])
        harm_jarjend.append(temp_jarjend)
                
    return [harmonic_mean(i) for i in harm_jarjend]



faili_nimi = input('Sisesta faili nimi: ')
andmed = []
with open(faili_nimi) as f:
    for rida in f:
        andmed.append(float(rida.split(',')[1].strip()))
        
plt.plot(range(1, len(andmed)+1), andmed)
plt.plot(range(1, len(andmed)+1), silu_andmed(andmed, 50))
plt.show()