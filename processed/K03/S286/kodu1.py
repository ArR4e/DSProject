aastatulu = float(input("Sisesta oma aastatulu: "))
if 0<aastatulu <= 6000:
    uustulu = round(aastatulu, 2)
    print("Teie maksuvaba tulu on " + str(uustulu) + " eurot.")
elif 6000<aastatulu<=14400:
    uustulu = 6000
    print("Teie maksuvaba tulu on " + str(uustulu) + " eurot.")
elif 14400<aastatulu<=25200:
    uustulu = round((6000-6000 / 10800 * (aastatulu-14400)), 2)
    print(uustulu)
elif aastatulu>25200:
    print("Teie maksuvaba tulu on 0 eurot.")
else:
    print("Sisestage mittenegatiivne arv")