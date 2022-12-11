from statistics import harmonic_mean
aktsiahinnad = []
aktsia = []
n = int(input("Sisesta n: "))
f = open("aktsiad.txt", "r")

def silu_andmed(aktsiahinnad, n):
    a = 0
    for i in f:
        rida = i.strip().split(", ", 1)
        aktsiahinnad.append(rida[1])
    intidena = list(map(float, aktsiahinnad))
    print(intidena)
    while a < n:
        keskmine = (a+1)/(1/sum(intidena[a]))
        aktsia.append(keskmine)
    return aktsia
#     a = 0
#     while a < n:
#         rida = f.readline().strip().split(",", 1)
#         keskmine = (a+1)/(1/float(sum())
#         aktsiad.append(keskmine)
#         a += 1
            

silu_andmed(aktsiahinnad, n)

print(aktsiahinnad)
print(aktsia)