from turtle import * #kutsub kilpkonna mängima
import random #toob juhuslikkuse mängu juurde

def hulknurk(külje_pikkus,külgede_arv):

    i=0
    speed(10)
    delay(0)

    penup()
    forward((külje_pikkus/2))
    pendown()

    while i< külgede_arv:
        
        right(360/külgede_arv)
        forward(külje_pikkus)
        i+= 1
#funktsioon määrab juhuslikuse alusel hulknurga külje pikkuse ja nurkade arvu

i=0
while i<30: #kordab 30 korda ja teeb 30 kujundit

    külje_pikkus= random.randint(1,200) #küljepikkus on juhuslik (200 enam-vähem mahub aknasse)
    külgede_arv= random.randint(3,20)#külgedearv on juhuslik vahemikus 3-20 (alla kolme ei saa)
    
    hulknurk(külje_pikkus, külgede_arv) # käivitab funktsiooni
    penup() #pliiats üles ja ostib uue koha
    
    n= (random.randint(1,2)) # see määrab juhuslikult, kas pööratakse vasakule või paremale
    if n==1:
        left(random.randint(0,360))
    else:
        right(random.randint(0,360))
    
    m= (random.randint(1,2)) #see määrab, liikumise suuna
    if m==1:
        forward(random.randint(1,200))
    else:
        backward(random.randint(1,200))
        
    i +=1 # liidab loendurisse, et määrata kujundite hulk
    pendown() #pliiats maha, et edasi joonistada


exitonclick() #saadab kilkonna koju ja sulgeb programmi