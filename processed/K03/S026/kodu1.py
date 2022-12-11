tulu = float(input("Palun sisesta aastatulu:"))


if tulu >= 25200:
    print("Maksuvaba tulu määr on: ", 0)
elif tulu >=14400:
    print("Maksuvaba tulu määr on: ", round(6000 - 6000 / 10800 * (tulu - 14400)))
elif tulu >=6000:
    print("Maksuvaba tulu määr on: ", 6000)
elif tulu >=0:
    print("Maksuvaba tulu määr on: ", round(tulu, 2))
else:
    print("Palun sisesta positiivne arv")