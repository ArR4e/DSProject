f = open("kinganumbrid.txt", "r")

while True:
    try:
        for rida in f:
            kinganr = float(rida.strip())
            nr = round(2/3*(kinganr-2))
            print(nr)
    except:
        print("Vigane sisend")