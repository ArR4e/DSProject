print("Tere, kallis kasutaja.")

from string import*
L = input("Palun kirjutage lähtefaili nimi: ")
S = input("Palun kirjutage sihtfaili nimi: ")

faill = open(L)
fails = open(S, 'w')
teisendamised = 0

for i in faill:
    teisendamised += i.count("Hello")
    teisendatud = i.replace("Hello", "Tere")   
    fails.write(teisendatud + '')

print("Tehti" + " " + str(teisendamised) + " " + "teisendamist")

faill.close()
fails.close()

