aastatulu = float(input("Sisesta aastatulu: "))


if aastatulu <0:
    print("Viga")
    maksuvaba = 0.
elif aastatulu <= 6000:
    maksuvaba = aastatulu
elif aastatulu <= 14400:
    maksuvaba = 6000
elif aastatulu <= 25200:
    maksuvaba = 6000 - 6000/10800*(aastatulu-14400)
else:
    maksuvaba = 0.


print("Maksuvaba tulu on", round(maksuvaba,2),"eurot.")