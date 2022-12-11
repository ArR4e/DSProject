fail = open("kinganumbrid.txt", "r")

for rida in fail:
    try:
        print(round(2/3*(float(rida)-2)), end="\n")
    except:
        print("Vigane sisend")
fail.close()