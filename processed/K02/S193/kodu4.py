from string import*

L = input("Palun sisestage lähtefaili nimi: " )
S = input("Palun sisestage sihtfaili nimi: ")

faill = open(L, "r")
fails = open(S, "w")
teisendamised = 0

for i in faill:
    teisendamised += i.count("Hello")
    teisendatud = i.replace("Hello", "Tere")
    fails.write(teisendatud)

print("Tehti" + str(teisendamised) +" "+ "teisendamist" )

faill.close()
fails.close()

