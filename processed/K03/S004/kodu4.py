with open("kinganumbrid.txt", "r") as file:
    tekst = file.read().splitlines()
for x in tekst:
    try:
        x = float(x)
        print(round(2/3*(x-2)))
    except ValueError:
        print("Vigane sisend")