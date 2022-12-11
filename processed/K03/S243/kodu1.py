#maksuvaba tulu
tulu=float(input("Sisesta aastatulu: "))
if tulu<0:
    print("Tulu peab olema positiivne!")
    tulu=float(input("Sisesta aastatulu: "))
if tulu < 6000:
    print("Maksuvaba tulu on ", round(tulu, 2), " eurot.")
elif 600 <= tulu < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif 14400<= tulu < 25200:
    maksuvaba = 6000 - 6000/10800*(tulu - 14400)
    print("Maksuvaba tulu on ", round(maksuvaba, 2), " eurot.")
else:
    print("Maksuvaba tulu on 0 eurot.")
    
    