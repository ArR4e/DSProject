aastatulu = float(input("Sisesta aastatulu ja saa maksuvaba tulu määr: "))
maksuvaba = 0

if aastatulu < 6000:
    maksuvaba = aastatulu
    
elif aastatulu >= 6000 and aastatulu <= 14400:
    maksuvaba = 6000

elif aastatulu > 14400 and aastatulu <= 25200:
    maksuvaba = 6000 - 6000/10800*(aastatulu - 14400)

else:
    maksuvaba = 0
    
print("Sinu maksuvaba tulu on:", round(maksuvaba, 2), "eurot")