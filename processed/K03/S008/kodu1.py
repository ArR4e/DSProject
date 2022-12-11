aastaPalk = float(input("Sisestage oma aastatulu: "))

if aastaPalk < 6000:
    print ("Maksuvaba tulu on " + str (round(aastaPalk, 2)))

elif aastaPalk >= 6000 and aastaPalk < 14400:
    print ("Maksuvaba tulu on " + str (round(aastaPalk - 6000, 2)))

elif aastaPalk >= 14400 and aastaPalk < 25200:
    print ("Maksuvaba tulu on " + str (round(6000 - (6000 / 10800) * (aastaPalk - 14400), 2)))

elif aastapalk > 25200:
    print ("Maksuvaba tulu on 0 eurot.")
    