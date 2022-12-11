fail = open('taksohinnad.txt', 'r',encoding='UTF-8')

sisu = fail.readlines()

a = 0

for rida in sisu:
    for number in rida:
        if number.isdigit() == True:
            a += float(number)
            
            
print(a)