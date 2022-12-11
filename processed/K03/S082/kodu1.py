maksuga = float(input("Sisesta aastatulu: "))

maksuvaba = 0

if maksuga < 6000:
    maksuvaba = maksuga

elif maksuga < 14400:
    maksuvaba = 6000
    
elif maksuga < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (maksuga - 14400)
    
elif maksuga >= 25200:
    maksuvaba = 0
    
    
    

print("Maksuvaba tulu on "+ str(round(maksuvaba, 2)) + " eurot.")