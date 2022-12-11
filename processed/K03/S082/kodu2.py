from pykkar import *

create_world("""

#########
#       #
#       #
#       #
#       #
#   <   #
#########

""")

while not is_wall():
    step()
    
right()

korda = 1
while korda <=4:
    while not is_wall():
        step()
    paint()
    right()
    korda +=1