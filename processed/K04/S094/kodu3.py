from turtle import *
def joonista(kylgarv, kyljepikkus):
    right(90)
    # kujund
    joonistatud = 0
    valmis = 0
    while(joonistatud < 11):
        down()
        forward(kyljepikkus)
        right(60)
        joonistatud += 1
        if (joonistatud >= 11):
            up()
            left(30)
            forward(200)
            right(90)
            joonistatud = 0
            valmis += 1
            if(valmis >= kylgarv):
                break
    
# alustab ülevalt 
up()
goto(-300, -300)
joonista(3, 50)

    
