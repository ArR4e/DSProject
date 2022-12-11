lähtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtfaili nimi: ")
inglisefail = open(lähtefail, "r",encoding='utf-8')
sisu = inglisefail.readlines()

def sisutõlge(sisu):
    asendused = 0
    list1 = []
    for a in sisu:
        asendused += a.count("Hello")
        a = a.replace("Hello", "Tere")
        list1.append(a)
    print("Tehti "+ str(asendused)+" asendust")
    return list1
 
eestifail1 = open(sihtfail, "w", encoding='utf-8')
eestifail1.writelines(sisutõlge(sisu))


eestifail1.close()
inglisefail.close()
    
