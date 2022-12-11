fail = open("kinganumbrid.txt", "r")

for kinganumber in fail:
    try:
        print(round(2/3*(float(kinganumber)-2)))
    except:
        print("Vigane sisend")
fail.close()
              