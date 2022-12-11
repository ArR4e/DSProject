e_nimi= input('Sisesta oma eesnimi: ')
p_nimi= input('Sisesta oma perekonnanimi: ')

e_nimi= e_nimi.lower()
p_nimi= p_nimi.lower()
#teeme kõik kohe väiketähtedeks

e_nimi=e_nimi.replace('ä','a')
e_nimi=e_nimi.replace('õ','o')
e_nimi=e_nimi.replace('ö','o')
e_nimi=e_nimi.replace('ü','u')

p_nimi=p_nimi.replace('ä','a')
p_nimi=p_nimi.replace('õ','o')
p_nimi=p_nimi.replace('ö','o')
p_nimi=p_nimi.replace('ü','u')

#eemaldame täpid

print('sinu kasutajanimi on:',e_nimi+'.'.strip()+ p_nimi)