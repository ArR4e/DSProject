f = open("kinganumbrid.txt")
while True:
    nr = f.readline()
    if str(nr) == '':
        break
    try:
        cm = (2 / 3 * (float(nr) - 2))
        print(str(round(cm)))
    except:
        print("Vigane sisend")
    

f.close()

