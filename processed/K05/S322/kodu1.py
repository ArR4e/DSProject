def tähednumbrid(parool):
    tähestik = "ABCDEFGHIJKLMNOPQRSŠZŽTUVWÕÄÖÜXYabcdefghijklmnopqrsšzžtuvwõäöüxy"
    numbrid = "0123456789"
    sis_tähti = False
    sis_numbreid = False
    # kontrolli kas paroolis on täh(t/-ed) ja numb(er/-rid)
    for täht in tähestik:
        if täht in parool:
            sis_tähti = True
            break
    for number in numbrid:
        if number in parool:
            sis_numbreid = True
            break
    # tagasta tingimuslause vastus (kas parool sisaldab numbreid ja tähti)
    return sis_numbreid and sis_tähti

def vaeseMeheKrüptograafia(parool):
    # koosta tagurpidi sõne
    uus = ""
    for i in range(len(parool)):
        uus += parool[-(i+1)]
    return uus

# küsi kasutajanimi
kasutajanimi = input("Sisestage kasutajanimi: ")

# defineeri kontrollmuutuja, mis saab True väärtuse
# ainult siis, kui kõik parooli jaoks vajalikud
# tingimused on täidetud
kontroll = False
# defineeri muutuja parooli jaoks (et hilisem kood saaks
# muutuja hiljem kätte)
parool = ""
while not kontroll:
    # küsi kasutajalt parool esimest korda
    parool = input("Sisestage parool: ")
    # küsi kasutajalt parool teist korda
    parool_verify = input("Sisestage parool uuesti: ")
    # kas esimene parool ei kattu teise parooliga?
    if not parool == parool_verify:
        print("Paroolid ei ühti. Proovige uuesti.")
    # kas sõne ei ole vähemalt 8 tähemärki pikk?
    elif not (len(parool) >= 8):
        print("Parool peab olema vähemalt 8 tähemärgi pikkune.")
    # kas sõnes puuduvad tähed või numbrid?
    elif not tähednumbrid(parool):
        print("Parool peab sisaldama tähti ja numbreid.")
    # kõikide eelmiste küsimuste vastus on eitav, st
    # kontrollid läbiti edukalt
    else:
        kontroll = True
# ava users.txt
kasutajad = open("users.txt", "a")
# pööra parool tagurpidi
krüptoParool = vaeseMeheKrüptograafia(parool)
# kirjuta kasutajanimi ja parool faili
kasutajad.write(f"{kasutajanimi}:{krüptoParool}\n")
# sulge users.txt
kasutajad.close()
