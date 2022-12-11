from math import*

tulu=float(input("Sisesta oma aastatulu:"))
while tulu<0:
    print("Sisestatud aastatulu ei saa olla negatiivne!")
    tulu=float(input("Sisesta oma aastatulu:"))
if tulu<14400:
    print("maksuvaba tulu on 6000 eurot.")
elif tulu<25200:
    print("Maksuvaba tulu on",round(6000-6000/10800*(tulu-14400), 2), "eurot.")
else:
    print("Maksuvaba tulu on 0 eurot")