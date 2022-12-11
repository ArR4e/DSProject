'''
[['O',' ',' ','X'],
 [' ','O','X',' '],
 [' ','X','O',' '],
 ['X',' ',' ','O']]


[['X','X','X',' '],
 [' ','O',' ',' '],
 [' ',' ','O',' '],
 [' ',' ',' ','O']]
 
[[' ',' ',' ',' '],
 [' ',' ',' ',' '],
 [' ',' ',' ',' '],
 [' ',' ',' ',' ']]
 
 


'''
def diagonaal(elemendid):
    for a in elemendid:
        print(a)
        if a  == []:
            print('tühi')
        if a[0]==0 or a[0] == 1 or a[1] == 1:
            print('jätkub')
        #siit peab edasi tegema seoses tegelikult peab lihtsalt a sees olema kas 0 või üks, üritan koodi edasi kirjutada nign kui vaja siis võin seletada ka




#diagonaal([[0, 2], [0, 1], [0, 2], [3]])

def vertikaal(elemendid):
    rida = 0
    uusnimekiri = [0, 0, 0, 0]
    for a in elemendid:
        for x in a:
            try: 
                b = uusnimekiri[x]
                d = b + 1
                uusnimekiri[x] = d
            except:
                break
            
    print('uusnimekiri: ' + str(uusnimekiri))
    jah = 0
    for a in uusnimekiri:
        if a >= 3:
            jah+=1
    return jah
    
    
def horisont(vahepealsed):
    if len(vahepealsed) >= 3:
        return True
    else:
        return False
    
#def vertikaal(elemendid):
    


def võitja(maatriks):
    ood = []
    
    xid = []
    kas_esineb = 0
    for a in maatriks:
        print(a)
        kordaja = 0
        ood_vahel=[]
        xid_vahel=[]
        for n in a:
            #print(n)
            if n == 'O':
                ood_vahel.append(kordaja)
            if n == 'X':
                xid_vahel.append(kordaja)
    
            kordaja += 1
        ood.append(ood_vahel)
        xid.append(xid_vahel)
        
        if horisont(ood_vahel) == True or  horisont(xid_vahel) == True:
            kas_esineb += 1
    kas_esineb += vertikaal(ood)
    kas_esineb += vertikaal(xid)
    
     
    print(ood)
    print(xid)
    print('horisontaalis(kas_esineb): ' + str(kas_esineb))
    
    
    
    
    
    
    
    
    
    
    
    
    
a = [['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]
    
print(võitja(a))
    
    
