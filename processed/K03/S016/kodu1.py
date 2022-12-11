at = float(input("Sisesta aastatulu: "))

if at < 6000:
    maksuvaba = at
elif 6000 <= at < 14400:
    maksuvaba = 6000
elif 14400 <= at <= 25200:
    maksuvaba = 6000-6000/10800*(at-14400)
else:
    at > 25200
    maksuvaba = 0

print("Maksuvaba tulu on: ", round(maksuvaba, 2))