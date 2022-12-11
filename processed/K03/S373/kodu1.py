aastatulu = float(input("Sisesta aastatulu: "))
if aastatulu < 6000:
    print("Maksuvaba tulu on " + aastatulu + " eurot.")
if aastatulu > 6000 and aastatulu < 14000:
    print("Maksuvaba tulu on " + str(6000) + " eurot.")
if aastatulu > 14400 and aastatulu < 25200:
   summa = round(6000-6000/10800*(aastatulu-14400), 2)
   print("Maksuvaba tulu on " + str(summa) + " eurot.")
if aastatulu > 25200:
    print("Maksuvaba tulu on " + str(0) + " eurot.")
          