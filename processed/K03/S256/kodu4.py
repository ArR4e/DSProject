fail = open("kinganumbrid.txt")
sisu = fail.readlines()
kogus = len(sisu)
#print(kogus)
i = 0
arv = 0
element = float(sisu[arv])
while i < kogus:
    try:
        element = float(sisu[arv])
        print(round((2/3)*(element - 2)))
        arv += 1
        i += 1
    except:
        print("Vigane sisend")
        i += 1
        arv += 1