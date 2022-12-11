tulu=float(input("Sisesta oma aasta tulu (positiivse arvuna):"))

if tulu<0:
    print("Aastatulu peab olema positiivne arv")
elif tulu<6000:
    print("Sinu aastatulu on", tulu)
elif tulu >= 6000 and tulu < 14400:
    print("Sinu maksuvaba aastatulu on 6000")
elif tulu>=14400 and tulu<25200:
    maksuvaba=round(6000 - 6000 / 10800 * (tulu - 14400),2)
    print("Sinu maksuvaba aastatulu on", maksuvaba)
elif tulu >= 25200:
    print("Sinu maksuvaba aastatulu on 0")


           