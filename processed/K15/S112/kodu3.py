
fail = input('Sisesta failinimi: ')
f = open(fail,'r',encoding = 'UTF-8')

väljumine = []
saabumine = []
hinnad = []

for rida in f:
    e = rida.strip().split(' ')
    väljumine.append(e[0])
    saabumine.append(e[1])
    hinnad.append(e[2])
    
f.close()


