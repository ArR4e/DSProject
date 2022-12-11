kinga_fail = open("kinganumbrid.txt", "r+")

for m in kinga_fail.readlines():
    try:
        uus_number = (float(m)-2)*2/3
        print(round(uus_number))
    except:
        print("Vigane sisend")

kinga_fail.close()

