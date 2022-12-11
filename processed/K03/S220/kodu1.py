aasta_tulu = float(input("Sisestage aastatulu "))

if aasta_tulu < 6000 :
    print("Maksuvaba tulu on", aasta_tulu, "eurot.")
elif aasta_tulu >= 6000 and aasta_tulu < 14400 :
    print("Maksuvaba tulu on 6000 eurot.")
elif aasta_tulu >= 14400 and aasta_tulu < 25200 :
    maksuvaba_tulu = round((6000 - (6000/10800 * (aasta_tulu - 14400))), 2)
    print("Maksuvaba tulu on", maksuvaba_tulu, "eurot.")
    
else :
    print("Maksuvaba tulu on 0 eurot.")