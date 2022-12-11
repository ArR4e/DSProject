tulu = float(input("Sisesta aastatulu:"))
if tulu <= 6000:
    print("Maksuvaba tulu on:", tulu)
elif 6000 < tulu < 14400:
    print("Maksuvaba tulu on: 6000")
elif 14400 <= tulu <= 25200:
    maks = round((6000-6000/10800*(tulu-14400)),2)
    print("Maksuvaba tulu on:", maks)
elif tulu > 25200:
    print("Maksuvaba tulu on: 0")