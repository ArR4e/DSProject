from pykkar import *

create_world("""
#########
#       #
#       #
#       #
#       #
#  >    #
#########
""")

while not is_wall() :
    step()

if is_wall() == True :
    right()

värvitud_põrandad = 0
while värvitud_põrandad <= 3:

    while not is_wall() :
        step()
    
    if is_wall() == True :
        paint()
        värvitud_põrandad += 1
        right()