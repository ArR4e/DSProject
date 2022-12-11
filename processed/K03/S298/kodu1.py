palk = float(input("plaunsisestage enda aastane sisse tulek: "))
tulu = 0
if palk <= 6000:
    tulu = palk
elif palk <= 14400:
    tulu = 6000
elif palk <= 25200:
    tulu = (6000 - 6000 / 10800 * (palk - 14400))
elif palk > 25200:
    tulu = 0

tulu = round(tulu, 2)
print("maksuvaba tulu on " + str(tulu) + " eurot")