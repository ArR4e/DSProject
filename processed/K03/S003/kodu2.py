from pykkar import*

create_world("""
########
#      #
#      #
#      #
#   <  #
#      #
########
""")

while not is_wall():
    step()
right()
nurgad = 0

while nurgad < 4:
    while not is_wall():
        step()
    paint()
    right()
    nurgad = nurgad + 1