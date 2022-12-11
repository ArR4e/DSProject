filename1, filename2 = input('Lähtefaili nimi:'), input('Sihtfaili nimi:')

with open(filename1) as f:
    content = f.read()
    
newcontent = content.replace('Hello',"Tere")

with open(filename2,'w+') as f2:
    f2.write(newcontent)
    
print("Tehti " + str(content.count('Hello')) + " asendamist.")