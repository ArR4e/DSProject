aastatulu = float(input("Sisesta aastatulu: "))
if aastatulu <= 6000:
    maksuvaba = round(aastatulu,2)
elif aastatulu <= 14400:
    maksuvaba = 6000
elif aastatulu <= 25200:
    maksuvaba = round(6000-6000/10800*(aastatulu-14400),2)
else:
    maksuvaba = 0
print("Maksuvaba tulu on", maksuvaba, "eurot.")
