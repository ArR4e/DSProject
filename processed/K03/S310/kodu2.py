from pykkar import *
create_world("""
########
#E      #
#       #
#       #
#       #
#       #
#########
""")


ilmakaar = get_direction()

if ilmakaar == 'N':
        right()
elif ilmakaar == 'W':
        right()
        right()
        
elif ilmakaar == 'S':
        right()
        right()
        right()
        
i = 0

while i < 3:
    # liigu seinani
    while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
        step()
    # värvi
    paint()
    i = i + 1
    # pööra 
    right()
    
    
    

    


