from pykkar import *

create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")



# liigub seinani
while not is_wall(): 
    step()

# pöörab ringi ja värvib ruudu
right()
paint()

if is_wall(): 
    step()
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



