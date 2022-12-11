aastatulu = int(input("Sisestage on aastatulu: "))
if aastatulu > 25200:
    maksuvaba = 0
elif aastatulu >= 14500:
    maksuvaba = (6000-(6000/10800)*(aastatulu-14400))
elif aastatulu >= 6000:
    maksuvaba = 6000
else:
    maksuvaba = aastatulu
print(round(maksuvaba,2))