aastatulu = float(input("Sisesta oma aastatulu: "))

if aastatulu <= 6000:
    print("Maksuvaba tulu on", aastatulu, "eurot.")
    
elif 6000 < aastatulu <= 14400:
    print("Maksuvaba tulu on 6000 eurot.")

elif 14400 < aastatulu <=25200:
    maksuvaba = round(6000 - 6000 / 10800 *( aastatulu -14400), 2)
    print("Maksuvaba tulu on", maksuvaba, "eurot.")
    
else:
    print("Maksuvaba tulu on 0 eurot.")