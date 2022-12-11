from pykkar import *
create_world("""
#######
#     #
#  <  #
#     #
#     #
#     #
#######""")
while not is_wall(): 
    step()

right()
while not is_wall():
    step()
paint()
for el in range(3):
    right()
    while not is_wall():
        step()
    paint()


