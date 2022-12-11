
failx = open("kinganumbrid.txt")
list=[]
for element in failx:
    list.append(element)
    uus = element.strip()
    if (uus.isnumeric()) == True:
        täisarv = int(uus)
        pikkus = 2/3 * (täisarv - 2)
        print(round(pikkus))
    else:
        try:
            float(uus)
            pikkus2 = 2/3 * (float(uus) - 2)
            print(round(pikkus2))
        except ValueError:
            print('Vigane sisend')

