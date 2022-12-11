f1 = open("kinganumbrid.txt", "w", encoding="UTF-8")
f1.write("25‎" + "\n")
f1.write("31" + "\n")
f1.write("kolmkümmend kaheksa" + "\n")
f1.write("42‎" + "\n")
f1.close()

f1 = open("kinganumbrid.txt")

suurus = f1.readline()
number = suurus.isnumeric()
f = suurus.strip()
cm = 2 / 3 * (f - 2)

while True:
    if suurus == "":
        break
    else:
        if number.strip():
            print(round(cm))
        else:
            print("Vigane sisend")