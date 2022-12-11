aastatulu = float(input("Sisesta aastatulu: "))

maksuvaba_tulu = 6000

while aastatulu < 0:
    aastatulu = float(input("Sisesta mittenegatiivne aastatulu: "))
if aastatulu < 6000:
    print("Maksuvaba tulu on " + str(aastatulu))
elif aastatulu >= 6000 and aastatulu <= 14200:
    print("Maksuvaba tulu on " + str(maksuvaba_tulu))
    
elif aastatulu > 14200 and aastatulu < 25200:
    maksuvaba_tulu = float(6000 - 6000 / 10800 * (aastatulu - 14400))
    print(round(maksuvaba_tulu, 2))
else:
    print("Maksuvaba tulu on 0")