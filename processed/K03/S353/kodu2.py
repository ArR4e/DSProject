from pykkar import *
import random
ridade_arv = random.randint(3,20) #siin saab muuta maailma võimalikku pikkust
veergude_arv = random.randint(3,20) #siin saab muuta maailma võimalikku laiust
prykkar= random.choice('<''>''v''^')
q = (veergude_arv) * (ridade_arv-2)
q1= (veergude_arv) * (ridade_arv-2)-1
q2= (veergude_arv-2) * (ridade_arv-2)
sone='#'*veergude_arv+'\n'
k2 = random.randint(1, q2)
while q>0:
    if q%veergude_arv ==0:
        sone+='#'
        q1-=1
    elif q%veergude_arv ==1:
        sone+=('#'+'\n')
        q1-=1
    elif k2==q2:
        sone+=prykkar
        q1-=1
        q2-=1
    else:
        sone+=' '
        q1-=1
        q2-=1
    q-=1
sone+='#'*veergude_arv

create_world(sone)
while not is_wall():
    step()
    
right()
'''
while not is_wall():
    step()
    
paint()

right()

while not is_wall():
    step()
    
paint()

right()

while not is_wall():
    step()
    
paint()

right()

while not is_wall():
    step()
    
paint()

right()
'''
i=4
while i>0:
    while not is_wall():
        step()
    paint()
    right()
    i-=1
right()
rigth()
