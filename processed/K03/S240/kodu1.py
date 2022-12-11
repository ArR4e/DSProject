palk = int(input("Sisesta oma aastatulu: "))
maksuvaba = 0

if palk < 6000:
    maksuvaba += palk
elif palk > 6000 and palk < 14400:
    maksuvaba = 6000
elif palk > 14400 and palk < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (palk - 14400)
elif palk > 25200:
    maksuvaba = 0
    

print ("Sinu maksuvaba tulu on: " + str(round(maksuvaba, 2)))