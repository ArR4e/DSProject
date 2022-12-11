from pykkar import*
create_world("""
#############
#>          #
#           #
#           #
#           #
#############
""")
paint()
while not is_wall():
    step()
right()
paint()
while not is_wall():
    step()
right()
paint()
while not is_wall():
    step()
right()
paint()
while not is_wall():
    step()
paint()

