aastatulu = float(input("Sisesta aastatulu: "))

def maksuvaba_tulu(aastatulu):
    if aastatulu <= 6000:
        return aastatulu
    elif 6000 < aastatulu <= 14400:
        return 6000
    elif 14400 < aastatulu < 25200:
        return 6000 - 6000/10800*(aastatulu - 14400)
    else:
        return 0
    
print("Maksuvaba tulu on ",round(maksuvaba_tulu(aastatulu),2), " eurot.")