x = input("Sisesta faili nimi")
y = input("Sisesta teine faili nimi")

with open(x) as f:
    fail = f.read()
    teisendused = fail.count("Hello")
    with open(y,"w") as e:
        e.write(fail.replace("Hello","Tere"))
   
print("Asenduste arv: " + str(teisendused)) 







