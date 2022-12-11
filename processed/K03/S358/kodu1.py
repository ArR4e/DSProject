#kodu1
aastatulu = float(input("Sisesta aastatulu: "))
while aastatulu <= 0:
    aastatulu = float(input("Proovi uuesti: "))
if aastatulu <= 6000:
    print("Maksuvaba tulu on: " + str(aastatulu))
elif aastatulu <= 14400:
    print("Maksuvaba tulu on: 6000")
elif aastatulu <= 25200:
    print("Maksuvaba tulu on: " + str(round(6000-6000/10800*(aastatulu-14400), 2)))
else:
    print("Maksuvaba tulu on: 0")