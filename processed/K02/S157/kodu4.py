fail1=input("Sisesta tõlgitav faili nimi:")
fail2=input("Sisesta fail kuhu tõlgitakse:")

f1=open(fail1,'r')
sonad=f1.read()
tolge1=sonad.replace("Hello",'Tere')
print(tolge1)
f2=open(fail2,'w')
tolge2=f2.write(tolge1)
kokku=sonad.count('Hello')
print(kokku)
f1.close()
f2.close()