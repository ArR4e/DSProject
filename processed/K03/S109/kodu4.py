fail = open("kinganumbrid.txt")
sisu1 = fail.readline()
try:
    arv = (int(2 / 3 * (sisu1 - 2)))
    print(arv)
except: 
    print("Vigane sisend")
fail.close()    