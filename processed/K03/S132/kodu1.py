while True:
    try:
        aasta_tulu = float(input("Sisestage oma aasta sissetulek(€): "))
        if aasta_tulu < 0:
            print("Negatiivne sissetulek pole lubatud")
            continue
        break
    except:
        print("Palun sisestada arv, proovime uuesti")
        
if aasta_tulu <= 6000:
    print(f"  Maksuvaba tulu on {round(aasta_tulu, 2)} €")
elif 6000 < aasta_tulu <= 14_400:
    print(f"  Maksuvaba tulu on 6000 €")
elif 14_400 < aasta_tulu <= 25_200:
    maksuvaba = 6000 - 6000 / 10_800 * (aasta_tulu - 14_400)
    print(f"  Maksuvaba tulu on {round(maksuvaba, 2)} €")
else:
    print(f"  Maksuvaba tulu on 0 €")