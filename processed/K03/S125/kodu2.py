from pykkar import *

create_world("""
########
#      #
#      #
#      #
#      #
#<     #
########
""")

suund = get_direction()
if suund == N:
    right()
elif suund == S:
    right()
    right()
    right()

nurki = 0
while nurki < 4:
    if not is_wall():
        step()
    else:
        paint()
        right()
        nurki += 1