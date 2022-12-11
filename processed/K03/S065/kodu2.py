from pykkar import *
create_world("""
#############
#           #
#           #
#           #
#    >      #
#           #
#############
""")
while not is_wall():
    step()
right()

for a in range(5):
    while not is_wall():
        step()
    right()
    paint()

