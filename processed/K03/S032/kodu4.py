f = open('kinganumbrid.txt')
 
while True:
    try:
        number = f.readline().strip()
        if number == "": break
        pikkus = 2/3*(float(number) - 2)
        print(round(pikkus))
    except:
        print("Vigane sisend")

