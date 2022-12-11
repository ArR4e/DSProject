def isfloat(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

file = open("kinganumbrid.txt","r")
lines = file.read().splitlines()

for kinganumber in lines:
    if isfloat(kinganumber):
        pikkus = 2/3 * (float(kinganumber) - 2)
        print(round(pikkus))
    else:
        print("Vigane sisend")
file.close()

