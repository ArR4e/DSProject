aastatulu = float(input("Sisesta aasta tulu: "))

while aastatulu >= 0:
    
    if aastatulu < 6000:
        print("Maksuvabatulu on", str(aastatulu), "eurot.")
        break
    
    elif aastatulu >= 6000 and aastatulu < 14400:
        print("Maksuvabatulu on", str(6000), "eurot.")
        break
    
    elif aastatulu >= 14400 and aastatulu < 25200:
        maksuvaba = 6000 - 6000 / 10800 * (aastatulu - 14400)
        print("Maksuvabatulu on", str(round(maksuvaba, 2)), "eurot.")
        break
    
    else:
        print("Maksuvabatulu on", str(0), "eurot.")
        break
        
else:
    print("Peate sisetama mittenegatiivse arvu.")
    
