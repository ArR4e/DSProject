import re

print("Kasutajanimed on:")

f = open("aadressid.txt", "r", encoding = "UTF-8")

for rida in f:
    korras_rida = rida.strip()
    if re.match('http://www.ut.ee/~', korras_rida):
        poolitus1 = korras_rida.split("~")
        kodulehekülg = poolitus1[0]
        sisaldab_kasutajanime = poolitus1[1]
        poolitus2 = sisaldab_kasutajanime.split("/")
        kasutajanimi = poolitus2[0]
        print(kasutajanimi)