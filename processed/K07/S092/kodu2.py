def cheapest(arg, km):
    name = ""
    for el in arg:
        el = el.split(",")
        try:
            if km * float(el[2]) + float(el[1]) < price:
                price = km * float(el[2]) + float(el[1])
                name = el[0]
        except:
            price = km * float(el[2]) + float(el[1])
            name = el[0]
    return name

file = open("taksohinnad.txt", encoding="UTF-8")
data = file.read().splitlines()
file.close()

km = float(input("Sisesta tee pikkus kilomeetrites: "))
print("Kõigi odavam on " + cheapest(data, km) + ".")