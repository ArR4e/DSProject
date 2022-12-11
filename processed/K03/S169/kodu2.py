from pykkar import *

create_world("""
########
#      #
#  <   #
#      #
#      #
#      #
########
""")


for a in range(4):
    while is_wall() != True:
        step()
    right()
    if is_wall() == True:
        paint()
    else:
        while is_wall() != True:
            step()
        paint()

        
        
            
        

