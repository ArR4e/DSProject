f1=input("Sisestage lähtefaili nimi: ")
f2=input("Sisestage sihtfaili nimi:")

f = open(f1, 'r', encoding="UTF-8")
f1=f.read()
print(f1)
f= open(f2, 'w',encoding="UTF-8")
f.write(f1)
"abcabca".count("ab")


f.close()










