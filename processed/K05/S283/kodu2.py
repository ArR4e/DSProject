import random
import string

def suurväike(sõne):
    uus_sõne = "" #tühi string, millesse hakatakse uut sõne kokku panema
    märgid = string.punctuation #muutujale märgid antakse väärtuseks kirjavahemärgid
    suvaline_märk = random.choice(string.punctuation) #muutujale suvaline_
    for i in sõne: #vaadatakse sõne sümboli kaupa läbi
        if i.isupper(): #suured tähed asendatakse väiksetega
            uus_sõne += i.lower()
        elif i.islower(): #väiksed tähed asendatakse suurtega
            uus_sõne += i.upper()
        elif i == " ": #kuna ka tühik on sõne osa on see vaja eraldi uue sõne sisse üle viia
            uus_sõne += " "
        elif i in märgid: #kui leitakse sõnest sümbol, asendatakse see eelnevalt loodud suvalise sümboliga
            uus_sõne += suvaline_märk
    return uus_sõne #tagastatakse tsükklis loodud uus sõne

sõne_sisend = input("Palun sisestage sõne: ")
print(suurväike(sõne_sisend))