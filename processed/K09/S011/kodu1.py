from statistics import harmonic_mean
import matplotlib.pyplot as plt 

#funktisioon
def silu_andmed(järjend, mitme_kaupa):
    a = järjend
    b = []
    x = 0
    while x <= mitme_kaupa:
        for el in a:
            Harmooniline_keskmine = [harmonic_mean(el)]
            b = b + Harmooniline_keskmine
            x +=1
    return (b)

#programm
andmed = open(input("Sisesta faili nimi: "))
arv = int(input("Sisesta mitme kaupa keskmistada: "))

andmed_jär = []
for rida in andmed_jär:
     kuupäeva_andmed = [(rida.split(","))]
     andmed_jär = andmed_jär +  kuupäeva_andmed[1]
     
silutud = silu_andmed(andmed_jär, arv)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(andmed_jär, silutud)
plt.show()