from pykkar import *
create_world("""
#######
# <   #
#     #
#     #
#     #
#     #
#######
""")

while not is_wall():
    step()
while is_wall():
    right()
while not is_wall():
    step()
paint()
while is_wall():
    right()
while not is_wall():
    step()
paint()
while is_wall():
    right()
while not is_wall():
    step()
paint()
while is_wall():
    right()
while not is_wall():
    step()
paint()
while is_wall():
    right()
exitonclick()