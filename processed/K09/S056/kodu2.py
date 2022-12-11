from statistics import harmonic_mean
import matplotlib.pyplot as plt
kuupäevad = []
kuupäevade = len(kuupäevad) #sellega saab paika graafiku alumised numbrid
hinnad = []
hindade = len(hinnad)

#failist sisselugemine
fail = input("Sisesta algandmete fail:")
failist_lugemine = open(fail)
for rida in failist_lugemine:
    read = rida.strip().split(", ")
    kuupäev = read[0]
    hind = read[1]
    kuupäevad.append(kuupäev)
    hinnad.append(hind)

#nii saab mehhaaniliselt, kui täisarvuks on kolm, see mis näiteks oli, pole aimu ka kuidas seda selle ülesande kohta teha
def silu_andmed(hinnad, n):
    keskmistatud_andmed = [harmonic_mean([hinnad[0]]), harmonic_mean(hinnad[0:n-1]), harmonic_mean(hinnad[0:n]), harmonic_mean(hinnad[n-2:n+1]), harmonic_mean(hinnad[n-1:n+2])]
    return keskmistatud_andmed

# üritasin hakata tegema graafikut, aga kuna mul neid keskimstatud andmeid ei ole siis ei tulnud välja 

# teen näite kohta mehhaaniliselt graafiku, lihtsalt et aru saada kuidas toimib
# arvud = [2, 1, 3, 4, 5]
# silutud_andmed = [2, 1.3333333333333333, 1.6363636363636365, 1.8947368421052633, 3.8297872340425534]
# kuud = [1, 2, 3, 4, 5]
# fig = plt.figure()
# ax = fig.add_subplot(1,1,1)
# ax.plot(kuud, arvud, label = "Arvud")
# ax.plot(kuud, silutud_andmed, label = "Silutud")
# ax.set_ylim(0, 5)
# ax.set_xticks([1, 2, 3, 4, 5])
# ax.legend()
# plt.show()