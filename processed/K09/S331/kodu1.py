import statistics
import matplotlib.pyplot as plt
def silu_andmed(järjend, n):
    järjend2 = []
    keskmistatud_järjend = []
    indeks = -1
    for el in järjend:
        järjend2.append(float(el))
        indeks += 1
        if len(järjend2) <= int(n):
            keskmine = statistics.harmonic_mean(järjend2)
            keskmistatud_järjend.append(float(keskmine))
        elif len(järjend2) > int(n):
            järjend3 = järjend2[(indeks+1-n):indeks+1]
            keskmine = statistics.harmonic_mean(järjend3)
            keskmistatud_järjend.append(float(keskmine))
    return(keskmistatud_järjend)
fail = input("Sisesta faili nimi:")
f = open(fail)
järjend = []
while True:
    rida = f.readline().strip()
    if rida == "":
        break
    rida1 = rida.split(", ")
    järjend.append(float(rida1[-1]))
    n = 50
print(järjend)
f.close()
#graafik
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(järjend)
ax.plot(silu_andmed(järjend, n))
plt.show()



        