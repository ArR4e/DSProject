from pykkar import *

create_world("""
########
#      #
#      #
#      #
#    > #
#      #
########
""")

while not is_wall():
    step()
if is_wall():
    right()
while not is_wall():
    step()
if is_wall():
    right()
if is_wall():
    right()
paint()
while not is_wall():
    step()
if is_wall():
    right()
paint()
while not is_wall():
    step()
paint()
if is_wall():
    right()
while not is_wall():
    step()
paint()
paint()


        


