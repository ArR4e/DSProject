failinimi = input('Sisesta failinimi: ')

fail = open(failinimi, encoding = 'UTF-8')

def võrdlus(fail):
    for rida in fail:
        väljumine, saabumine, hind = rida.strip().split(' ')
        
        if väljumine > min1:
            