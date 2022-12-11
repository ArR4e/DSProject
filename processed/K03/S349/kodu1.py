aastatulu = float(input("Palun sisesta enda aastatulu: "))
if aastatulu < 6000:
    maksuvaba_tulu = aastatulu
else:
    if aastatulu >= 6000 and aastatulu < 14400:
        maksuvaba_tulu = 6000
    else:
        if aastatulu >= 14400 and aastatulu < 25200:
            maksuvaba_tulu = float(6000 - 6000 / 10800 * (aastatulu - 14400))
        else:
            if aastatulu > 25200:
                maksuvaba_tulu = 0
                
maksuvaba_tulu_ümardatuna = round(maksuvaba_tulu, 2)
print("Sinu maksuvabatulu on " + str(maksuvaba_tulu_ümardatuna) + " eurot.")
                
