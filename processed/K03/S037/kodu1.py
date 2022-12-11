aastatulu = input("Sisesta aastatulu: ")

tulu = float(aastatulu)

if tulu <= 6000:
    lõplik  = round(tulu, 2)

elif 6000 < tulu <= 14400:
    lõplik = 6000

elif 14400 < tulu <= 25200:
    tulu = 6000 - 6000 / 10800 * (tulu - 14400)
    lõplik  = round(tulu, 2)
    
else:
    lõplik = 0
    
print("Maksuvaba tulu on " + str(lõplik) + " eurot.")