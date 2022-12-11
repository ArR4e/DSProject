from pykkar import *
create_world("""
#################
#               #
#               #
#               #
#   >           #
#               #
#               #
#               #
#               #
#################
""")
while not is_wall():
    step()
right()
x = False
while not x:
    while not is_wall():
        step()
    x= is_painted()
    paint()
    right()
    step()

exitonclick()