fail1 = str(input("Sisesta 1. faili nimi: "))
fail2 = str(input("Sisesta 2. faili nimi: "))

with open(fail1, 'rt') as f1:
    with open(fail2, 'wt') as f2:
        for rida in f1:
            f2.write(rida.replace('Hello', 'Tere'))
with open(fail1, 'rt') as f1:
    x = f1.read()
    y = x.count('Hello')
print(y)            


    
