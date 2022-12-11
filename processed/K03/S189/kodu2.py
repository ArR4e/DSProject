from pykkar import *
create_world("""
########
#      #
# <    #
#      #
#      #
#      #
########
""")
while not is_wall():
    step()
right()
step()
paint()
right()
times = 1
while times <= 4:
    while not is_wall():
        step()
    times +=1
    right()
    paint()


