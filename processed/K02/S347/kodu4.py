a = input("Sisesta l2htefaili nimi:")
b = input("Sisesta sihtfaili nimi:")
fail1 = open(a, encoding = "UTF-8")
fail2 = open(b, "w", encoding= "UTF-8")
fail2.write(fail1.read().replace("Hello!", "Tere"))
vahetused = b.count("Tere")
print(int(vahetused))
fail1.close()
fail2.close()