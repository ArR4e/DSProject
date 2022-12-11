fail_1 = input("Lähtefaili nimi: ")
fail_2 = input("Sihtfaili nimi: ")

vana = open(fail_1, 'r')
uus = open(fail_2, 'w')
for line in vana:
    uus.write(line.replace("Hello", "Tere"))
    
x = open(fail_2, 'r')
y = x.read()
print(y)


    
vana.close()
uus.close()

