from pykkar import *

create_world("""
#########
#       #
#       #
#       #
#       #
#       #
#       #
#      >#
#########
""")

while not is_wall():
    step()
else:
    right()
while True:
    if is_painted():
        break
    elif is_wall():
        paint()
        right()
        step()
    else:
        step()
while True:
    right()

    