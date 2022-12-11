#Maksuvaba tulu
aastatulu = float(input("Sisesta aastatulu: "))
maksuvaba_tulu = 0
if aastatulu < 6000 :
    print("Maksuvaba tulu on " + str(round(aastatulu, 2)) + " eurot.")
elif aastatulu >= 6000 and aastatulu < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
elif aastatulu >= 14400 and aastatulu < 25200:
    maksuvaba_tulu = 6000-6000/10800*(aastatulu-14400)
    print("Maksuvaba tulu on " + str(round(maksuvaba_tulu, 2)) + " eurot.")
else:
     print("Maksuvaba tulu on 0 eurot.")   