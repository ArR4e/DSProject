aastatulu = float(input("Sisestage palun oma aastatulu: "))

while aastatulu < 0:
    aastatulu = float(input("Aastatulu ei saa olla negatiivne. Proovige uuesti: "))
    
if aastatulu <= 6000:
    print("Sinu maksuvaba tulu on", aastatulu, "eurot.")
    
elif 6000 < aastatulu <= 14400:
    print("Sinu maksuvaba tulu on 6000 eurot.")
    
elif 14400 < aastatulu <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (aastatulu - 14400)
    print("Sinu maksuvaba tulu on", round(maksuvaba, 2), "eurot.")

else:
    print("Sinu maksuvaba tulu on 0 eurot.")

