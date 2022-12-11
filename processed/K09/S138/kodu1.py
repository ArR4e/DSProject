import matplotlib.pyplot as plt
f = open("aktsiad.txt").readlines()
väärtused = []
päevad = []
for i in f:
    i = i.split(",")
    väärtused.append(float(i[-1]))
    päevad.append(i[0])
def silu_andmed(arvud,n):
    silutud_arvud = []
    if n < 1: return
    a = 1
    siluma = 0
    for j,i in enumerate(arvud):
        for x in range(a):
            siluma+=1/arvud[j-x]
        silutud_arv = a/siluma
        silutud_arvud.append(silutud_arv)
        siluma = 0
        if a < n:
            a+=1
    return silutud_arvud

plt.plot(päevad,väärtused)
plt.plot(päevad,silu_andmed(väärtused,50))
plt.show()