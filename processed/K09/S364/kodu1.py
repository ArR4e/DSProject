from statistics import harmonic_mean
import csv
import matplotlib.pyplot as plt

def silu_andmed(x, y):
    list1 = []
    list2 = []
    jär = x[:]
    for i in x:
        list2.append(jär.pop(0))
        if len(list2) > y:
            list2.pop(0)
        keskmistatud = harmonic_mean(list2)
        list1.append(keskmistatud)
    return list1

stocks = []
time = []
date = []

list2 = input("Sisesta faili nimi: ")
fail = open(list2, "r")
for rida in fail:
    rea = rida.strip('\n').split(', ')
    stocks.append(float(rea[1]))
    time.append(float(rea[1]))
y=50
fail.close()

profit = stocks
list1 = silu_andmed(stocks, y)
profit2 = list1
date = [i for i in range(1, len(time)+1)]

end = plt.figure()
k = end.add_subplot(1, 1, 1)
k.plot(date, profit)
k.plot(date, profit2)
k.set_yticks([0.0000, 0.0025, 0.0050, 0.0075, 0.0100, 0.0125, 0.0150, 0.0175])
k.set_xlim(1, len(time) + 50)
plt.show()




        