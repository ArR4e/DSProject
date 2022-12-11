fail = open("kinganumbrid.txt")

read = fail. readlines()

for rida in read:
    try:
        kinganumber = float(rida)
        jalalaba = round(2/3 * (kinganumber -2))
        print(jalalaba)
    except:
        print("Vigane sisend")

fail.close()