from pykkar import *

def liigu():
    while not is_wall(): #liigub kuni tuleb sein
        step()
    paint() #värvib
    right()

#suvaline maailm
create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")

for i in range(4): #neli nurka
    liigu()