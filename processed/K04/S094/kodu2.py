def summa(num1,num2):
    valem_lugeja = num1 + num2
    valem_nimetaja = 1+num1*num2/299792.458**2
    esimene_summa = valem_lugeja / valem_nimetaja
    return esimene_summa

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
esimese_summa = summa(u,v)
teine_summa = summa(esimese_summa, x)
kolmas_summa = summa(teine_summa, y)
print("Kiiruste summa on " + str(kolmas_summa) + " km/s")