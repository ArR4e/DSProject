lähtefail = str(input("Sisesta lähtefaili nimi kujul 'faili_nimi.txt': "))
sihtfail = str(input("Sisesta sihtfaili nimi kujul 'faili_nimi.txt': "))
while True:
    tulemus_1 = lähtefail.endswith('.txt')  
    tulemus_2 = sihtfail.endswith('.txt')  
    if tulemus_1 and tulemus_2:
        print("Mõlemad failinimed on õigel kujul.")
        break
    else:
        lähtefail = str(input("Sisesta lähtefaili nimi kujul 'faili_nimi.txt': "))
        sihtfail = str(input("Sisesta sihtfaili nimi kujul 'faili_nimi.txt': "))
try:
    def asenda_f(tekst):     
        tekst = tekst.replace("Hello", "Tere")
        return(tekst)

    def loe_f():
        tekst = inglise.read()
        asendamised = tekst.count("Hello")
        print("Tehti", asendamised, "asendamist.")
        return tekst
   
    eesti = open(sihtfail, 'r')   
    inglise = open(lähtefail, 'r')
    with open(sihtfail, 'w') as ee:
        ee.writelines(asenda_f(loe_f()))
finally:
    inglise.close()
    eesti.close()
    