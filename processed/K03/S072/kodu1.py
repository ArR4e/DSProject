aastatulu = float(input("Sisetage aastatulu: "))

if aastatulu < 6000.0:
    maksuvaba = aastatulu
elif 6000.0 <= aastatulu < 14400.0:
    maksuvaba = 6000.0
elif 14400.0 <= aastatulu < 25200.0:
    maksuvaba = 6000.0 - ((6000.0 / 10800.0) * (aastatulu - 14400.0))
else:
    maksuvaba = 0
    
print("Maksuvaba tulu on " + str(round(maksuvaba, 2)) + " eurot.")
    