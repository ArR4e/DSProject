from statistics import harmonic_mean
y = open('aktsiad.txt', encoding ='UTF-8')
b = []

    
#def silu_andmed(a, b):
x = []
c = 1
f = 0
d = 0   
#b = [1, 2, 3, 4, 5, 6, 7]
#a = harmonic_mean([1, 2, 3, 4])
#print(a)
def silu_andmed(a, b):
   while True:
       
        rida = y.readline().strip()
        if rida =='':
            break
        uus = rida.split(',')
        b +=[float(uus[1])]
   
   
   while f < len(b):
        x.append(harmonic_mean(b[d:c]))
        c +=1
        if 3<c:
            d +=1
    
        f +=1

print(b)
b = x
print(b)

    