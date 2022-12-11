aastatulu = float(input("Sisesta aastatulu: "))

maksuvaba_tulu = 6000-(6000/10800)*(aastatulu-14400)
maksuvaba_tulu = str(maksuvaba_tulu)
                  
if aastatulu < 6000:
    print("Maksuvaba tulu on võrdne aastatuluga.")
elif aastatulu <= 14400 and aastatulu >= 6000:
    print("Maksuvaba tulu on 6000 eurot")

elif aastatulu > 14400 and aastatulu <= 25200:
        print("Maksuvaba tulu on " + maksuvaba_tulu + " eurot")
else:
    print("Maksuvaba tulu on 0 eurot")
