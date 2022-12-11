a = abs(float(input("Sisestage oma aasta tulu: ")))
vaba = 6000

if a <= 6000:
    print("Teie maksuvaba tulu on", round(a, 2), "eurot.")
elif a <= 14400:
    print("Teie maksuvabatulu on", round(vaba, 2), "eurot.")
elif 14400 < a <= 25200:
    vaba = round(vaba - vaba / 10800 * (a - 14400), 2)
    print("Teie maksuvabatulu on", vaba, "eurot.")
else:
    print("Teie maksuvabatulu on 0 eurot.")
    