aastatulu = float(input("Sisesta aastatulu: "))
if aastatulu < 14401 :
    tulu = 6000
elif 14399 < aastatulu < 25201:
    tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
else :
    tulu = 0
print("Maksuvaba tulu on" , round(tulu, 2) , "eurot.")
