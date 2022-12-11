from pykkar import*

create_world("""
########
#      #
#  v   #
#      #
#      #
########
""")
m = get_direction()
if m == 'E':
    right()
    right()
    right()
elif m == 'W':
    right()
elif m == 'S':
    right()
    right()
while not is_wall():
    step()
    if is_wall():
        right()
        while not is_wall():
            step()
            while is_wall():
                paint()
                right()
    
