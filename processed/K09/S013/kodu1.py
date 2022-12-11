from statistics import harmonic_mean
import matplotlib.pyplot as plt

f=input("Sisesta faili nimi")
fail=open(f,"r", encoding="UTF-8")
järjend= []
for rida in fail:
    rida=rida.strip("\n")
    rida=rida.split(",")
    järjend.append(float(rida[1]))
    
def silu_andmed(a,b):
    silutud_järjend= []
    lisajärjend = []
    for rida in a:
        lisajärjend.append(rida)
        if len(lisajärjend) > b:
            lisajärjend.pop(0)
       
           
            
        silutud_järjend.append(harmonic_mean(lisajärjend))
        
    return silutud_järjend

    
      



fig= plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(järjend)
ax.plot(silu_andmed(järjend,50))
 
plt.show()

fail.close()