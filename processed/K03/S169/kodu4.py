fail = open("kinganumbrid.txt","r",encoding="utf8")

read = fail.readlines()

for a in read:
    a.strip()
    try:
       jalapikkus = 2/3 * (float(a)-2)
       print(round(jalapikkus))
    except:
        print("vigane sisend")


fail.close()