fail=open('kinganumbrid.txt', 'r')
while True:
    try:
        pikkus1 = int(2/3 * (float(fail.readline()) - 2))
        break
    except:
        print("Vigane sisend")
while True:
    try:
        pikkus2 = int(2/3 * (float(fail.readline()) - 2))
        print(round(pikkus2))
        break
    except:
        print("Vigane sisend")
fail.close()




