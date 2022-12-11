fail_1 = input("Lähtefaili nimi: ")
fail_2 = input("Sihtfaili nimi: ")
c = open("fail_1.txt")
print(c.read().count("hello"))

d = open("fail_2.txt" ,"w")
txt = c.read()
d.write(txt.replace("hello","tere" + "\n"))
d.close()

d = open("fail_2.txt")
print(d.read().count("tere"))