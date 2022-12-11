from pykkar import*
create_world("""
#############
#           #
#           #
#      >    #
#           #
#           #
#############
""")
while True:
    while not is_wall():
        step()
    if is_wall():
        paint()
    right()
    

    
