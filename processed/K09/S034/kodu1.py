from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(algandmed_järjendina, täisarv):
    
    loendus = 1
    tabeli_andmed1 = []
    sisu = []
    algne_tingimus = 0 #mitmes arv hetkel käsil on (indeksi järgi)
    pikkus = len(algandmed_järjendina)
    for el in algandmed_järjendina:
        if algne_tingimus + 1 <= täisarv:
            sisu += [el]
        elif algne_tingimus + 1 > täisarv:
            del sisu[0]
            sisu += [el]
            ###
            global z
            z = sisu
            ####
        keskmine = harmonic_mean(sisu)
        algandmed_järjendina[algne_tingimus] = keskmine
        ###
        global x
        x = algandmed_järjendina
        ###
        algne_tingimus += 1
        if algne_tingimus != pikkus:
            continue
        else:
            while True:
                loendus < len(algandmed_järjendina)
                tabeli_andmed1 += [loendus]
                ##
                global y
                y = tabeli_andmed1
                
                    
                ####
                loendus += 1
                if loendus > len(algandmed_järjendina):
                    break              
 
 
algandmed_järjendina_0 = input("Palun sisesta algandmed järjendina: ")
täisarv_1 = int(input("Palun sisesta täisarv mitme elemendi kaupa keskmistamist rakendatakse: "))

baas =[]
algandmed_järjendina1 = algandmed_järjendina_0.strip('[]')
algandmed_järjendina2 = algandmed_järjendina1.split(', ')
algandmed_järjendina =[]
for element in algandmed_järjendina2:
    algandmed_järjendina += [float(element)]
silu_andmed(algandmed_järjendina, täisarv_1)

#graafik
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
            
ax.plot(y, z)
ax.plot(y, x)
            
ax.set_xlabel("Tabel")       
plt.show() 