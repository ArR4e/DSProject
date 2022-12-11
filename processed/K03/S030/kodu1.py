tulu=float(input("Sisesta aastatulu: "))
tulu=abs(round(tulu, 2))
if tulu < 6000:
    print("Maksuvaba tulu on " + str(tulu)+ " eurot.")
elif tulu >= 6000 and tulu < 14400:
          print("Maksuvaba tulu on 6000.00 eurot.")
elif tulu >=14400 and tulu < 25200:
    tulu=abs(round((6000-6000/10800*(tulu-14400)), 2))
    print("Maksuvaba tulu on " + str(tulu)+ " eurot.")
elif tulu >= 25200:
    print("Maksuvaba tulu on 0.00 eurot.")