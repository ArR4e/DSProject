fail1 = open(input("Sisesta lähtefaili nimi: "))
fail2 = open(input("Sisesta sihtefaili nimi: "), "a")
uusfail = ""
word = "Hello"
kordus = 0
for i in fail1:
    i = i.strip()
    if word in i:
        uusfail = i.replace("Hello","Tere")
        fail2.write(uusfail+"\n")
        uusfail = ""
        kordus = kordus + i.count("Hello")
fail2.close()
print(kordus)