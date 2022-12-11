maksuvaba = float(input("Sisesta aastatulu: "))
if maksuvaba < 6000:
    print("Maksuvaba tulu on ", round(maksuvaba, 2), " €.")
elif maksuvaba >= 6000 and maksuvaba < 14_400:
    print("Maksuvaba tulu on 6000.00 €.")
elif maksuvaba >= 14_400 and maksuvaba < 25_200:
    maksuvaba = 6000 - 6000 / 10_800 * (maksuvaba - 14_400)
    print("Maksuvaba tulu on ", round(maksuvaba, 2), " €.")
else:
    print("Maksuvaba tulu on 0 €!")