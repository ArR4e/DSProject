AastaTulu = float(input("Sisesta aastatulu: "))

if AastaTulu <= 6000:
    MaksuvabaTulu = AastaTulu
elif AastaTulu <= 14400:
    MaksuvabaTulu = 6000
elif AastaTulu  <= 25200:
    MaksuvabaTulu = 6000 - 6000 / 10800 * (AastaTulu - 14400)
else:
    MaksuvabaTulu = 0
    
print("Maksuvaba tulu on",  round(MaksuvabaTulu, 2), "euort.")
    