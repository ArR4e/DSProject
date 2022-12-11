tulu = input("Palun Sisestage oma aastatulu: ")
tulu = abs(float(tulu))
if tulu < 6000:
    print("Teie maksuvaba tulu on ",str(round(tulu, 2)) +" eurot.")
elif tulu >= 6000 and tulu < 14400:
    print("Teie maksuvaba tulu on 6000 eurot")
elif tulu >= 14400 and  tulu < 25200:
    print("Teie maksuvaba tulu on ",str(round(6000-6000/10800*(tulu-14400), 2)) +" eurot.")
elif tulu >= 25200:
    print("Teie maksuvaba tulu on 0 eurot.")