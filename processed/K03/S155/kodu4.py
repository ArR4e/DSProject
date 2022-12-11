f = open('jalad.txt')
while True: 
    algne = f.readline().strip()
    if algne == "":
        break 
    try:
        number = float(algne)
        pikkus = round(2/3 * (number - 2))
        print(pikkus)
    except ValueError:
        print("Vigane sisend")
f.close()