sissetulek=float(input("Sisesta sissetulek: "))
mvaba=0
if sissetulek<0:
    print("Sissetulek ei saa olla negatiivne")
elif sissetulek <= 6000:
    print("Maksuvaba tulu on " + str(round(sissetulek, 2)) + ".")
elif sissetulek > 6000 and sissetulek <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif sissetulek > 14400 and sissetulek <=25200:
    mvaba=6000 - (6000 / 10800 * (sissetulek - 14400))
    print("Maksuvaba tulu on " + str(round(mvaba, 2)) + ".")
elif sissetulek > 25200:
    print("Maksuvaba tulu on 0.")