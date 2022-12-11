aastatulu = float(input("Sisesta aastatulu: "))
if 0 < aastatulu < 6000:
    print ("Maksuvaba tulu on võrdne aastatuluga.")
elif 6000 <= aastatulu < 14400:
    print ("Maksuvaba tulu aastas on 6000 eurot.")
elif 14400 <= aastatulu < 25200:
    maksuvaba_tulu = (6000 - 6000 / 10800 * (aastatulu - 14400))
    vastus = round(maksuvaba_tulu, 2)
    print(vastus)
elif aastatulu < 0:
    print ("Viga.")
else:
    print ("Maksuvaba tulu on 0 eurot.")