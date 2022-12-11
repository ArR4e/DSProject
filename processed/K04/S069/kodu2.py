u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input('Teise keha kiirus esimese keha suhtes on: '))
x = float(input('Kolmanda keha kiirus teise keha suhtes on: '))
y = float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))
arv = 0
def summa(b, a):
    kiirus = (b+a)/(1+(b*a/(299792.458**2)))
    print(kiirus)
    global arv
    arv += kiirus
a = v
b = u
summa(b, a)
a = x
b = v
summa(b, a)
a = y
b = x
summa(b, a)
print('Kõik kiirused kokku:', arv)