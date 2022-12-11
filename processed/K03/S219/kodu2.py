from pykkar import *

#Test world

create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")


while is_wall() == False:
    step()
    
right()

while is_wall() == False:
    step()
    
paint()
right()

while is_wall() == False:
    step()
    
paint()
right()

while is_wall() == False:
    step()
    
paint()
right()

while is_wall() == False:
    step()
    
paint()