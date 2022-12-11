vana_fail = input("Sisestage algfaili asukoht: ")
uus_fail = input("Uue faili nimi kuhu tõlge läheb: ")

fail1 = open(vana_fail, encoding="UTF-8")
fail2 = open(uus_fail, "w")

vana_fail = Hello.replave('Hello', 'Tere')