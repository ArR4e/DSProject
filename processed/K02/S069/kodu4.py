a = open(input("Sisesta lähtefaili nimi: "), 'r')
fail = open(input("Sisesta sihtfaili nimi: "), 'w+')
txt = a.read()
k = txt.count("Hello")
print("nii mitu vahetust tehti:", k)
uus = txt.replace('Hello', 'Tere')
fail.write(uus)   
fail.close()







