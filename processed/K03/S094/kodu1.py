aastatulu = abs(float(input("Sisesta aastatulu: ")))
maksuvaba = 0

if(aastatulu <= 6000):
    maksuvaba = aastatulu
    print("Maksuvaba tulu on " + str(maksuvaba) + " eurot.")
    
elif(aastatulu > 6000 and aastatulu <= 14400):
    maksuvaba = 6000
    print("Maksuvaba tulu on " + str(maksuvaba) + " eurot.")
    
elif(aastatulu > 14400 and aastatulu <= 25200):
    maksuvaba =  6000 - 6000 / 10800 * (aastatulu - 14400)
    print("Maksuvaba tulu on " + str(round(maksuvaba, 2)) + " eurot.")
    
else:
    maksuvaba = 0
    print("Maksuvaba tulu on " + str(maksuvaba) + " eurot.")