#ei saa aru miks automaatkontrollis tagastab
#tühja järjendi. Thonny's töötab normaalselt
import matplotlib.pyplot as plt
useralg = str(input("Sisesta faili nimi: "))
f = open(useralg, encoding="UTF-8")
global algaktsiad
algaktsiad = []
xlist = []
while True:
    
    rida = f.readline()
    
    if len(rida) > 0:
        aktsia = rida.strip("\n")
        aktsiaa = aktsia.split(", ")
        aktsiaaa = aktsiaa[1]
        algaktsiad.append(float(aktsiaaa))
    else:
        f.close()
        break

def silu_andmed(alg, täisarv):
    
    t = 1
    dragger = 0 - täisarv
    silutud = []
    määratud = -55

    while True:
        try:
            xlist.append(t)
            jagatav = 0
            if dragger < 0:
                for i in range(0, t):
                    jagatav += 1/(alg[i])
            if dragger == 0:
                määratud = t - 1
            if dragger >= 0:
                for i in range((dragger + 1), t): #draggerile +1 list indexi omapärasuste tõttu
                    jagatav += 1/alg[i]
            
            if määratud == -55:
                kesk = t/jagatav
            if määratud != -55:
                kesk = määratud/jagatav
           
            silutud.append(kesk)
            
            t += 1
            dragger +=1
        except:
            return silutud
    
#print(silu_andmed(algaktsiad, 50))


plt.plot(algaktsiad)
plt.plot(silu_andmed(algaktsiad, 50))

plt.show()
        