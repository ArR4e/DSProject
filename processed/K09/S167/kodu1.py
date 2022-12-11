from statistics import harmonic_mean
import matplotlib.pyplot as plt
# x:y

andmed = input("Mis on algandmete faili nimi:")
#x = [2, 1, 3, 4, 5]
#y = 0

def silu_andmed(x, n):
    list = []
    
    n = n - 1
    
    y = 0
    i = 0
    for el in range(0, len(x)):
        if el <= n:
            y = harmonic_mean(x[i:el+1])
        if el > n:
            i += 1
            y = harmonic_mean(x[i:el+1])
        list.append(y)
    return list

#print(silu_andmed([2, 1, 3, 4, 5], 3))


o = open(andmed, 'r')
o1 = open(andmed, 'r')

def p_päev():
    list = []
    i = 0
    while True:
        f = o.readline().strip()      
        if f == "":
            break
        list.append(i)
        i += 1
    return list


def h_hind():
    list = []
    while True:
        f_list = []
        f = o1.readline().strip()
        if f == "":
            break
        
        for i in f:
            f_list.append(i)
        
        while f_list[0] != ",":
            f_list.pop(0)        
        f_list.pop(0)
        f_list.pop(0)
        
        väärtus = f_list
        
        list.append(väärtus)
    return list



päev = p_päev().copy()
hind = h_hind().copy()

o = []
string = ""
for i in hind:
    string = ""
    for i1 in i:
        string += i1
    n = float(string)
    o.append(n)

#-------------

plt.plot(päev, o)

silelist = silu_andmed(o, 50)

plt.plot(päev, silelist)

plt.show()