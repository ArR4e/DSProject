#Maksuvaba tulu
while True:
    try:
        tulu = float(input("Palun sisesta aastatulu: "))
        if tulu <= 6000 and tulu >= 0:
            maksuvaba = round(tulu, 2)
            break
        elif tulu > 6000 and tulu <= 14400:
            maksuvaba = 6000.00
            break
        elif tulu > 14400 and tulu <= 25200:
            maksuvaba = round(6000 - 6000 / 10800 * (tulu - 14400), 2)
            break
        elif tulu > 25200:
            maksuvaba = 0.00
            break
        else:
            print("Sisestasid negatiivse arvu. Proovi uuesti")
    except:
        print("Kas oled kindel, et sisestasid arvu?")
           
    
print("Maksuvaba tulu on " + str(maksuvaba) + " eurot.")
