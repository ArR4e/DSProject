file1 = input("Sisesta sisendfaili nimi: ")
file2 = input("Sisesta väljundfaili nimi: ")

with open(file1, "r") as f:
    f_sisu = f.read()
    asendusi = f_sisu.count("Hello")
    f_sisu = f_sisu.replace("Hello", "Tere")
    
with open(file2, "w") as f:
    f.write(f_sisu)
    
print(asendusi)