from pykkar import *

create_world("""
################
#              #
#              #
#              #
#     <        #
################
""")

varvida = 4
while varvida > 0:
    if not is_wall():
        step()
    elif is_wall():
        paint()
        right()
        varvida -= 1
        
    
            
            
            
        
        