from pykkar import *

#Kasutan hetkel suvalist maailma, kuid toimib ka erineva pikkuse/laiuse ning alguspositsiooni korral

create_world("""
#########
# v     #
#       #
#       #
#       #
#       #
#       #
#########
""")

i = 0

while is_wall():
    right()
    
while not is_wall():
    step()
    if is_wall() and i == 0:
        while is_wall():
            right()
        i += 1
    elif is_wall() and i < 4:
        paint()
        right()
        i += 1
    elif is_wall() and i == 4:
        paint()
        break
    
        
    
