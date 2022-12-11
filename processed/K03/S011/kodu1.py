sissetulek = float(input("Sisesta aastatulu: "))
maksuvabatulu = 0
if 0 < sissetulek < 6000 :
    maksuvabatulu = sissetulek
    print("Maksuvaba tulu on ", maksuvabatulu, "eurot")
elif 6000 <= sissetulek < 14400:
    maksuvabatulu += 6000
    print("Maksuvaba tulu on ", maksuvabatulu, "eurot")
elif 14400 <= sissetulek < 25200 :
    maksuvabatulu += (6000 - (6000 / 10800) * (sissetulek - 14400))
    maksuvabatulu = round(maksuvabatulu, 2)
    print("Maksuvaba tulu on ", abs(maksuvabatulu), "eurot")
elif sissetulek >= 25200 :
    print("Maksuvaba tulu on 0 eurot")