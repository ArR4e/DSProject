Lähtefail = input("Lähtefaili nimi: ")
Sihtfail = input("Sihtfaili nimi: ")
fail1 = open(Lähtefail)
list = []
for read in fail1:
    list.append(read)
    
list2 = []
m = 0
for rida in list:
    m += rida.count('Hello')
    x = rida.replace('Hello', 'Tere')
    list2.append(x)
    
  
    
fail2 = open(Sihtfail, 'w')
fail2.writelines(list2)


fail2.close()

print("Tehti " + str(m) + " asendamist.")



