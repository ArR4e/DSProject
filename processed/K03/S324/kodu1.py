aastatulu = float(input("Sisesta aastatulu: "))

if aastatulu < 6000:
    maksuvaba = aastatulu

elif aastatulu >= 6000 and aastatulu < 14400:
    maksuvaba = 6000
    
elif aastatulu >= 14400 and aastatulu <= 25200:
    maksuvaba = 6000 - (6000 / 10800) * (aastatulu - 14400)
    
elif aastatulu > 25200:
    maksuvaba = 0
    
print("Maksuvaba tulu on " + str(round(maksuvaba, 2)) + " eurot.")