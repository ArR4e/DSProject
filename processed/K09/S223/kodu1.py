import matplotlib.pyplot as plt

def väga_harmooniline_keskmine(arvud):
    arvud = [1/arvud[x] for x in range(len(arvud))]
    ultra_harmooniline_keskmine = len(arvud)/sum(arvud)
    return ultra_harmooniline_keskmine

def silu_andmed(data, n):
    sillutis = []
    for x in range(1,len(data)+1):
        if x-n < 0:
            start = 0
        else:
            start = x-n
        sillutis += [väga_harmooniline_keskmine(data[start:x])]
    return sillutis

file = str(input("Sisestage faili nimi: "))
with open(file, "r", encoding="utf-8") as f:
    data = f.readlines()
data = [float(x.strip().split(", ")[1]) for x in data]

graph_new = silu_andmed(data, 50)
graph_old = data

plt.plot(graph_old)
plt.plot(graph_new)
plt.show()