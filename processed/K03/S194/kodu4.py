with open("kinganumbrid.txt") as f:
    while True:
        ridade_list = f.read().splitlines()
        for i in ridade_list:
            try:
                print(round((float(i)-2)*(2/3)))
            except:
                print("Vigane sisend")
        break
