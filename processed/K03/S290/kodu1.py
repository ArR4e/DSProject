aastatulu = int(input("Sisesta aastatulu: "))
if aastatulu <= 6000:
    print (input("Maksuvaba tulu on " + str(aastatulu) + " eurot."))
if 6000 < aastatulu <= 14400:
    print (input("Maksuvaba tulu on 6000 eurot aastas."))
if 14400 < aastatulu <= 25200:
    n = 6000 - 6000 / 10800 * (aastatulu - 14400)
    print ("Maksuvaba tulu on " + str(round(n, 2)) + " eurot.")
if 25200 < aastatulu:
    print ("Maksuvaba tulu on 0 eurot.")
