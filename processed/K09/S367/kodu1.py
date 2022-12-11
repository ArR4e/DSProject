from statistics import harmonic_mean

f = open('andmed.txt', 'r')
a = []
for rida in f:
    järjend = f.readline.split(' ')
    a.append(järjend[1])
b = len(a)

def silu_andmed(a, b):
    uus = []
    vastus = []
    for element in range(len(a)):
        if b < element:
            for i in range(element-b,b+1):
                uus.append(a[i])
            vastus.append(harmonic_mean(uus))
        else:
            for i in range(0, element+1):
                uus.append(a[i])
            vastus.append(harmonic_mean(uus))
    return vastus
        
f.close()
    
        