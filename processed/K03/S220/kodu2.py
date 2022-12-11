from pykkar import*
create_world("""
########
#      #
#      #
#   v  #
#      #
#      #
########
""")

for i in range(2):
    while not is_wall() :
        step()
    right()
for i in range(3):
    paint()
    while not is_wall() :
            step()
    right()
paint()
