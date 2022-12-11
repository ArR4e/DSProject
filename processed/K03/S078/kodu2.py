from pykkar import *

create_world("""
#########
#<      #
#       #
#       #
#       #
#       #
#########
""")

i = 0
y  = 0
print(get_direction())
while not is_wall():
    step()
while is_wall() == True:
    right()

while not is_wall() and i < 4:
    step()
    if is_wall() == True:
        i += 1
        paint()
        right()
            