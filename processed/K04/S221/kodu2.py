u = float(input('Kui kiirelt liigub esimene keha?'))
v = float(input('Kui kiirelt liigub teine keha esimese suhtes?'))
x = float(input('Kui kiirelt liigub kolmas keha teise suhtes?'))
y = float(input('Kui kiirelt liigub neljas keha kolmanda suhtes?'))
c = float(299792.458)
def summa(k, l):
    ü = k + l
    am = 1 +((k * l) / (c ** 2))
    global vastus
    vastus = ü / am

esimene = summa(u, v)
teine = summa(vastus, x)
kolmas = summa(vastus, y)

print('Kiiruste summa on ', vastus, " km/s" )
    