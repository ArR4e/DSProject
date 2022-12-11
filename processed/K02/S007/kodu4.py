
a = input("Lähtefaili nimi: ")
b = input("Sihtfaili nimi: ")


f = open(a)
ingliskeelne = f.read()
f.close()

eestikeelne = ingliskeelne.replace("Hello", "Tere") 


f = open(b, "w")
f.write(eestikeelne)
f.close()

x = ingliskeelne.count('Hello')
print("Tehti",x ,"asendamist.")