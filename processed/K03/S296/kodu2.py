from pykkar import *

create_world("""
#############
#           #
#      >    #
#           #
#           #
#           #
#############""")
if is_wall():
    right()
    
while not is_wall():
    step()
if is_wall():
    right()

while not is_wall():
    step()
paint() 

right()
while not is_wall():
    step()
paint()

right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint()
right()
while not is_wall():
    step()
paint() 
