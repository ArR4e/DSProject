from statistics import harmonic_mean
import matplotlib.pyplot as plt

def loe_andmed(faili_nimi):
    read = []
    try:
        f = open(faili_nimi)
        read = []
        for rida in f:
            v = rida.split(",")
            read = read + [float(v[1].strip())]
        
        f.close()
        
        return read
    except:
      return read
      

def silu_andmed(jarjend, n):
    keskmistatud_andmed = []
    keskmiste_jarjend = []
    
    jarjendi_pikkus = len(jarjend)
    
    i = 0
    while i < jarjendi_pikkus:
      if i > n-1:
        keskmiste_jarjend.pop(0)
        keskmiste_jarjend.append(jarjend[i])
        keskmistatud_vaartus = harmonic_mean(keskmiste_jarjend)
      else:    
        keskmiste_jarjend.append(jarjend[i])
        keskmistatud_vaartus = harmonic_mean(keskmiste_jarjend)
        
      keskmistatud_andmed.append(keskmistatud_vaartus)
      i+=1
    
    return keskmistatud_andmed

def naita_graafik(silumata_jarjend, keskmistatud_andmed):
    andmete_jarjend = list(range(1, len(keskmistatud_andmed)+1))

    fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
    ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.

    ax.plot(andmete_jarjend, silumata_jarjend)
    ax.plot(andmete_jarjend, keskmistatud_andmed)

    plt.show()                   # Kuvame joonise ekraanile.

##################################
    
algandmete_fail = input("Sisesta algandmete faili nimi:")

silumata_jarjend = loe_andmed(algandmete_fail)

if len(silumata_jarjend) < 1 :
    print("Sisestatud faili ei leitud voi see on tyhi.")
else:
    keskmistatud_andmed = silu_andmed(silumata_jarjend, 50)
    naita_graafik(silumata_jarjend, keskmistatud_andmed)

