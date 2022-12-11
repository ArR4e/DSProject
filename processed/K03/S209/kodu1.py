aastatulu = int(input("Sisesta aastatulu: "))

tuluvaba = 0

if aastatulu <= 6000:
    tuluvaba = aastatulu
    
elif aastatulu > 6000 and aastatulu <= 14400:
    tuluvaba = 6000

elif aastatulu > 14400 and aastatulu <= 25200:
    tuluvaba = round(6000 - 6000 / 10800 * (aastatulu - 14400), 2)
    
print("Maksuvaba tulu on: ", tuluvaba, "eurot")