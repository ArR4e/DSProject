from pykkar import *
create_world("""
########
#      #
#      #
#   <  #
#      #
#      #
########
""")

counter = 0
while not is_wall(): 
    step()
   
right()
while True:
    while not is_wall():
        step()
    paint()
    counter += 1
    if counter == 4:
        break
    right()