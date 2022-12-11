from turtle import *

def ruutude_fraktal(aste,pikkus):
    if aste != 0:
        for i in range(4):
            forward(pikkus)
            if i != 3:
                if aste > 0:
                    ruutude_fraktal(-aste+1,pikkus*0.5)
                else:
                    ruutude_fraktal(-aste-1,pikkus*0.5)
            if aste > 0:
                right(90)
            else:
                left(90)
            

speed(0)
ruutude_fraktal(4,100)
done()