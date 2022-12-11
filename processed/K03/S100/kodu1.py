aastatulu = float(input("Sisestage aastatulu: "))

if aastatulu < 6000:
    mvtulu = aastatulu
elif 6000 <= aastatulu < 14400:
    mvtulu = 6000
elif 14400 <= aastatulu < 25200:
    mvtulu = 6000-6000/10800*(aastatulu-14400)
else:
    mvtulu = 0

print(f"Maksuvaba tulu on {round(mvtulu, 2)} eurot.")