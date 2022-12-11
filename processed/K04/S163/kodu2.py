keha1 = float(input('Esimese keha kiirus vaatleja suhtes on: '))
keha2 = float(input('Teise keha kiirus esimese keha suhtes on: '))
keha3 = float(input('Kolmanda keha kiirus teise keha suhtes on: '))
keha4 = float(input(' Neljanda keha kiirus kolmanda keha suhtes on: '))

c_ruut = 299792.458**2

def summa(u, v):
    summa = (u + v)/(1+((u * v)/c_ruut)) 
    return summa

print('Kiiruste summa on ' + str(summa(summa(summa(keha1,keha2),keha3), keha4)) + ' km/s')