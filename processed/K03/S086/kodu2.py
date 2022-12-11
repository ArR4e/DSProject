#Pykkar värvib ristkülikukujulise maailma kõik nurgad

from pykkar import *

#Testimiseks
create_world("""
##############
#            #
#            #
#      ^     #
#            #
#            #
##############
""")

while not is_wall(): #Liigub kuni tuvastab seina enda ees
    step()

right() #Pöörab paremale, suund arbitraarne

for i in range(4): #On juba ristküliku ääres, liigub kuni jõuab seinani (järelikult on nurgas), värvib selle ja pöörab (kordab seda iga külje jaoks)
    while not is_wall():
        step()
    paint()
    right()
    