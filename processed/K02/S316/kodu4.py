lähtefail = open(input("Sisesta lähtefaili nimi: "))
sihtfail = input("Sisesta sihtfaili nimi: ")

lähtefail.read()

f = open(sihtfail, "w")

korduste_arv = 0
f.write("Hello".replace("Hello", "Tere" + "!" + "\n"))
korduste_arv = "tere".count("tere")

f.write("Hello".replace("Hello", "Tere" + " "))
korduste_arv = korduste_arv + "tere".count("tere")

f.write("friend".replace("friend", "sõber" + "!" + "\n"))
korduste_arv = korduste_arv + "sõber".count("sõber")

f.write("Nice".replace("Nice", "Tore" + " "))
korduste_arv = korduste_arv + "Tore".count("Tore")

f.write("see".replace("see", "näha" + " "))
korduste_arv = korduste_arv + "näha".count("näha")

f.write("you".replace("you", "sind" + "!"))
korduste_arv = korduste_arv + "sind".count("sind")


print("Tehti" + " " + str(korduste_arv) + " " + "teisendust")


lähtefail.close()
f.close()
