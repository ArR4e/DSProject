sissetulek = float(input("Sisesta oma aastatulu: "))

if sissetulek <= 6000:
    print("Teie maksuvaba tulu on ", sissetulek, " eurot aastas")
elif 6000 < sissetulek <= 14400:
    print("Teie maksuvaba tulu on 6000 eurot aastas")
elif 14400 < sissetulek <= 25200:
    maksuvaba = round((6000 - (6000/10800)*(sissetulek - 14400)),2)
    print("Teie maksuvaba tulu on ", maksuvaba, " eurot aastas")
elif sissetulek > 25200:
    print("Teie maksuvaba tulu on 0 eurot aastas")
