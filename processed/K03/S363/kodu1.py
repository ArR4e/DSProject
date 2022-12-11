aasta = float(input("Palun sisesta aastatulu: "))

if aasta < 6000:
    maksuvaba = aasta
    
if aasta >= 6000 and aasta < 14400:
    maksuvaba = 6000.00
    
if aasta >= 14400 and aasta < 25200:
    maksuvaba = 6000 - 6000 / 10800 * (aasta - 14400)
    
if aasta >= 25200:
    maksuvaba = 0
    
print("Maksuvaba tulu on", round(maksuvaba, 2), "eurot.")
