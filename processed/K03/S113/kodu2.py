from pykkar import *

create_world("""
##########
#        #
#     <  #
#        #
#        #
#        #
##########
""")

while not is_wall():
    step()

right()

while not is_wall():
    step()

right()
paint()
while not is_wall():
    step()
    
right()
paint()
while not is_wall():
    step()
    
right()
paint()
while not is_wall():
    step()
    
right()

while not is_wall():
    paint()
