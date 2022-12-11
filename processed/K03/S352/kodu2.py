from pykkar import*
create_world("""
########
#    v #
#      #
#      #
#      #
#      #
########
""")

while True:
    step()
    if is_wall():
        right()
        break
while True:
    while not is_wall():
        step()
    if is_wall():
            right()
            paint()