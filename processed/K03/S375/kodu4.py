fail = open("kinganumbrid.txt", "r", encoding="UTF-8")
for rida in fail:
    try:
        print(str(round((2/3)*(float(rida) - 2))))
    except:
        print('Vigane sisend')
        