f= open("kinganumbrid.txt", encoding = "UTF-8")

for rida in f:
    try:
        print (round((2/3 * (float(rida) - 2))))
    except:
        print("vigane sisend")