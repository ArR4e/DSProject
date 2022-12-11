aastatulu = float(input("Sisesta aastatulu: "))
if aastatulu < 6000:
    print("Maksuvaba tulu on "+str(aastatulu)+" eurot.")
elif aastatulu < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif aastatulu < 25200:
    a = (round((6000 - (6000 / 10800) *(aastatulu - 14400)), 2))
    print("Maksuvaba tulu on "+str(a)+" eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")