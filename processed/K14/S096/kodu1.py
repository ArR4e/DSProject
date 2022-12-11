# Rekursiivne absoluutväärtus

def rek_abs(järjend):
    uus_järjend = []
    if len(järjend) == 0:
        return uus_järjend
    else:
        for i in järjend: #Käib läi järjendi elemendid ning vaatab kas element on list või mitte
            if isinstance(i, list):  #Kui element on list, siis kutsub funktsiooni uuesti välja sama elemendiga
                uus_järjend.append(rek_abs(i))
            else:  #Kui element ei ole list, siis võetakse selle abs. väärtus ja lisatakse uude listi
                uus_järjend.append(abs(i))
        return uus_järjend  #Lõpuks väljastatakse uus järjend, kus säilib andmestruktuur

l = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
print(rek_abs(l))