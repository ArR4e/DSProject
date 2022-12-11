u = input("Esimese keha kiirus vaatleja suhtes: ")
v = input("Teise keha kiirus vaatleja suhtes: ")
x = input("Kolmanda keha kiirus vaatleja suhtes: ")
y = input("Neljanda keha kiirus vaatleja suhtes: ")

def summa(u, v):
    c = 299792.458 ** 2
    return u + v
print("kiiruste summa on " + str(summa(u, v)))

summa() 