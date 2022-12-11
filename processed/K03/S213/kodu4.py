numbrid_fail = open("kinganumbrid.txt", "r")
numbrid_list = list(numbrid_fail.readlines())
for x in numbrid_list:
    try:
        x = float(x)
        x = 2 / 3 * (x - 2)
        print(round(x))
    except ValueError:
        print("Vigane sisend")
