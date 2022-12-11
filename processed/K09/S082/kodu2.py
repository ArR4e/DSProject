from random import randint

def minu_shuffle(nimekiri):
    vahepealne = []
    #print('algne list: ' + str(nimekiri))
    for a in nimekiri:
        n = randint(0,1)
        if n == 0:
            #print('ei tee midagi')
            True
        elif n==1:
            vahepealne = nimekiri
            x = randint(0, len(nimekiri)-1)
            vahetatav = nimekiri[x]
            nimekiri[nimekiri.index(a)] = vahetatav
            nimekiri[x] = a
            #print('vahetatakse: '+str(a) + ' kohale ' + str(vahetatav) + ' hetkel list: ' + str(nimekiri) )
        
        #vahepealne.append(n)
        
        
    #return nimekiri
            
    
    
    
    
nimekiri = [1, 3, 3, 4, 5, 5, 5, 6, 6]
minu_shuffle(nimekiri)