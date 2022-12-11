tulu = float(input("Sisesta aastatulu: "))

if tulu <= 6000 :
    print("Maksuvaba tulu v6rdne aastatuluga -", tulu ,"eurot.")
elif 6000 < tulu <= 14400:
    print("Makusvaba tulu 6000 eurot aastas.")
elif 14400 < tulu <= 25200:
    maksuvaba = round(6000 - 6000 / 10800 * (tulu - 14400), 2)
    print("Maksuvaba tulu on ",maksuvaba ,"eurot.")
else:
    print("Maksuvaba tulu 0 eurot")