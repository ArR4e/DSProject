#kodu1 - maksuvaba tulu
aastatulu = abs(float(input("Sisesta oma aastatulu: ")))
if aastatulu <= 6000:
   print("Maksuvaba tulu on " + str(round(aastatulu, 2)))
elif aastatulu > 6000 and aastatulu <= 14400:
    print("Maksuvaba tulu on 6000.00 eurot.")
elif aastatulu > 14400 and aastatulu <= 25200:
    print("Maksuvaba tulu on " + str(round(6000-6000/10800*(aastatulu-14400), 2)))
else:
    print("Maksuvaba tulu on 0.00 eurot.")
          
          
          