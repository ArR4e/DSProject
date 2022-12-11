from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(järjend,arv):
    korras_järjend = []
    for el in järjend:
        indeks = järjend.index(el)
        if indeks+1-arv<=0:
            a = järjend[:indeks+1]
            korras_järjend = korras_järjend + [harmonic_mean(a)]
        else:
            a = järjend[indeks+1-arv:indeks+1]
            korras_järjend = korras_järjend + [harmonic_mean(a)]
    return(korras_järjend)
                
fail = input("Failinimi: ")
with open(fail) as f:
    andmed = f.readlines()
    n=50
    x_telg=[]
    for anne in andmed:
        if anne == "\n":
            break
        else:
            anne_korras = anne.strip("\n")
            anne_korras = anne_korras.split(", ")
            ainult_anne=float(anne_korras[-1])
            x_telg= x_telg+[ainult_anne]
    
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(x_telg)
ax.plot(silu_andmed(x_telg,n))
plt.show()

    