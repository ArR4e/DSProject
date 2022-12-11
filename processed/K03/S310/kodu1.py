# veidi segaseks jäi, kas 6000 ja 14400 on kuni kaasa arvatud või mitte kaasa arvatud

# automaatne kontroll kahjuks ei töötanud - annab errorit:
# You are using an encrypted connection.
# To use an encrypted connection with the execution servers it is required you accept its certificates.
# If you have problems with this process, you can try to use a http (unencrypted) connection or other browser.
# Please, click on the following links (server #) and accept the offered certificate.
# Server 10

aastatulu = float(input('Sisesta oma aastatulu:'))

if aastatulu < 6000:
    maksuvaba_tulu = aastatulu

elif aastatulu >= 6000 and aastatulu < 14400:
    maksuvaba_tulu = 6000
    
elif aastatulu >= 14400  and aastatulu <= 25200:
    maksuvaba_tulu = 6000 - 6000 / 10800 * (aastatulu - 14400)
    
else:
    maksuvaba_tulu = 0
    
print(round(maksuvaba_tulu, 2))
