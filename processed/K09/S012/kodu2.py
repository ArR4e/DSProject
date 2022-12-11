#kodu2 - minu shuffle
import random
def minu_shuffle(a):
    for i in a: #käin iga elemendi listis läbi, võib kasutada ka range(len(a)
                #aga hetkel pole vahet
        b = random.choice(a)#valin listist a suvalise elemendi
        a.append(b)#lisan selle elemendi olemasolevasse listi
        a.remove(b)# eemaldan sellesamuse elemendi, et list ei muutuks kahekordseks
        


    
        
    