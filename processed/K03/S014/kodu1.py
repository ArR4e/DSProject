tulu=float(input("Sisesta enda aastatulu: "))


if tulu<6000:
    print("Maksuvaba tulu on "+str(round(tulu, 2))+" eurot. Soovitan ühendust võtta kohaliku omavalitsuse sotsiaaltöötajaga, kes saab nõu ja jõuga abistada!")
elif 6000<=tulu<14400:
    print("Maksuvaba tulu on 6000,00 eurot. Ehk soovid teha tööampse, et pisut lisa teenida? Loe selle kohta Töötukassa kodulehelt!")
elif 14400<=tulu<25200:
    print("Maksuvaba tulu on "+str(round(6000-6000/10800*(tulu-14400),2))+" eurot. Jätka samas vaimus!")
else:
    print("Maksuvaba tulu on 0 eurot. Palju õnne suure aastase sissetuleku puhul! Sinu makstud maksud aitavad kaasa tasuta koolihariduse kättesaadavusele:))")
          