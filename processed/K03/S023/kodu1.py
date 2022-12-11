aastatulu = float(input("Sisestage aastatulu:"))
if aastatulu < 6000:
    print("Maksuvaba tulu on",aastatulu,"eurot.")
if aastatulu >= 6000 and aastatulu < 14400:
    print("Maksuvaba tulu on 6000 eurot.")
if aastatulu >= 14400 and aastatulu <25200:
    maksuvaba = 6000 - 6000/10800 * (aastatulu - 14400)
    print("Maksuvaba tulu on",round(maksuvaba, 2),"eurot.")
if aastatulu >= 25200:
    print("Maksuvaba tulu on 0 eurot.")
