readFileName = open(input("Palun sisestage lähtefaili nimi: "))
writeFileName = open(input("Palun sisestage sihtfaili nimi: "), "w")
replaceString = "Tere"
replace = readFileName.read().replace("Hello", replaceString)
print("Tehti", replace.count(replaceString), "asendamist.")
writeFileName.write(replace)
writeFileName.close()
readFileName.close()

