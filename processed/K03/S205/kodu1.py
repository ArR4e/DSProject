while True:
    tulu = input("Sisesta oma aastatulu: ")
    try:
        tulu = float(tulu)
        if (tulu < 0):
            print("Aastatulu peab olema positiivne")
            continue
        else:
            break
    except ValueError:
        print("Aastatulu peab olema number!")
        continue
if (tulu<=6000):
    print("Maksuvaba tulu on " + str(round(tulu, 2))+"€")
elif (tulu <= 14400):
    print("Maksuvaba tulu on 6000€")
elif (tulu <= 25200):
    print("Maksuvaba tulu on " + str(round(6000-6000/10800*(tulu-14400), 2))+"€")
else:
    print("Maksuvaba tulu on 0€")