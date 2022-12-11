kinganumber = open("kinganumbrid.txt")

while True:
    try:
        for line in kinganumber:
            m = float(line)
            jalalaba_pikkus = 2/3 * (m - 2)
            print(round(jalalaba_pikkus))
    except:
        print("Vigane sisend")


kinganumber.close()