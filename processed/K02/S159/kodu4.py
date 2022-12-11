engfile = input('Palun sisestada lähtefaili nimi: ')
estfile = input('Palun sisestada sihtfaili nimi: ')

feng = open(engfile, encoding='UTF-8')
fest = open(estfile, "w", encoding='UTF-8')

vahetusi = 0

for ridu in feng:
    vahetusi += ridu.count('Hello')
    fest.write(ridu.replace('Hello', 'Tere'))
    
    
feng.close()
fest.close()
 
print('Vahetati kokku ' + str(vahetusi) + ' sõna!')
 
 
 
 
#f = open(file, r), 'Hello'.replace('Tere'), 'abcabcab'.count('ab')