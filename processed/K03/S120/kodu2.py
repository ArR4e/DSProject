from pykkar import *

create_world("""
########
#     ^#
#      #
#      #
#      #
#      #
########
""")

while True:
    if is_wall():
        right()
        break
    step()

painted = 0
done = False
while not done:
    if is_wall():
        right()
        paint()
        painted += 1
    step()
    if painted >= 4:
        done = True
    