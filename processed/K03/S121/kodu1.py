a = float(input("Sisesta aastatulu: "))
if a <= 6000:
    print("Maksuvaba tulu on " + str(a))
elif 6000 < a <= 14400:
    print (" Maksuvaba tulu on 6000 eurot")
elif 14400 < a <= 25200:
    print(" Maksuvaba tulu on " + str(round(6000-6000/10800*(a-14400), 2)) + " eurot")
else:
    print(" Maksuvaba tulu on 0 euro")