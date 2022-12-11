# Maksuvaba tulu
aastatulu = float(input("Sisests aastatulu:"))
if aastatulu <= 6000:
    print("Maksuvaba tulu:" + str(aastatulu))
elif 6000 < aastatulu <= 14400:
    print("Maksuvaba tulu:" + str(6000))
elif 14400 < aastatulu <= 25200:
    print("Maksuvaba tulu:" + str(round(6000 - (6000 /
10800 * (aastatulu - 14400)))))
elif aastatulu > 25200:
    print("Maksuvaba tulu:" + str(0))