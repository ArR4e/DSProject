eesnimi = str(input("Sisesta eesnimi: "))
perenimi = str(input("Sisesta perenimi: "))
print((eesnimi+'.'+perenimi)\
.replace('õ','o').replace('Õ','o')\
.replace('ö','o').replace('Ö','o')\
.replace('ü','u').replace('Ü','u')\
.replace('ä','a').replace('Ä','a')\
.lower())