x = float(input("Sisesta aastatulu: "))

if 0 <= x < 6000:
    maksuvaba = x
    print("Maksuvaba tulu on " + str(maksuvaba) + " eurot.")
    
elif 6000 <= x < 14400:
    maksuvaba = 6000
    print("Maksuvaba tulu on " + str(maksuvaba) + " eurot.")
    
elif 14400 <= x <= 25200:
    maksuvaba = 6000 - 6000 / 10800 * (x-14400)
    y = round(maksuvaba, 2)
    print("Maksuvaba tulu on " + str(y) + " eurot.")
    
elif 25200 < x:
    maksuvaba = 0
    print("Maksuvaba tulu on 0 eurot.")
    
else:
    print("Aastatulu ei saa olla negatiivne arv.")