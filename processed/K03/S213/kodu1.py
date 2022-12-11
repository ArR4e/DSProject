tulu = float(input("Sisesta aastatulu: "))
if (tulu < 0):
    print("Tulu peab olema positiivne arv!")
elif (tulu <= 6000):
    print("Maksuvaba tulu on " + str(round(tulu, 2)) + " eurot.")
elif (tulu > 6000 and tulu < 14400):
    print("Maksuvaba tulu on 6000 eurot." )
elif (tulu > 14000 and tulu < 25200):
    arvutus = 6000 - 6000 / 10800 * (tulu - 14400)
    print("Maksuvaba tulu on " + str(round(arvutus, 2)) + " eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")