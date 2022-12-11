import math

a_tulu = float(input("Sisestage aastatulu "))
try:
    if a_tulu <= 6000:
        print("Maksuvaba tulu on ", round(a_tulu, 2), " eurot.")
    elif a_tulu <= 14400:
        print("Maksuvaba tulu on 6000 eurot.")
    elif a_tulu <= 25200:
        print("Maksuvaba tulu on ", round(6000 - 6000 / 10800 * (a_tulu - 14400), 2)," eurot.")
    elif a_tulu > 25200:
        print("Maksuvaba tulu on 0 eurot.")
except:
    print("Midagi läks valesti. Proovige programm uuesti käivitada!")