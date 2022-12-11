a = input('fail1')
b = input('fail2')

f1 = open(a, 'r', encoding='UTF-8')
f2 = open(b, 'w', encoding='UTF-8')

kogus = 0
for rida in f1:
    kogus += rida.count('Hello')
    f2.write(rida.replace('Hello', 'Tere'))
print('tehti', kogus, 'asendust.')
    
f1.close()
f2.close()


