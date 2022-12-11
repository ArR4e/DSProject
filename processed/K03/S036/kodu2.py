from pykkar import*

create_world("""
#######
#     #
#>    #
#     #
#     #
#     #
#     #
#######
""")


def turn_right():
    right()
def paint_x():
    
    paint()

def go_to_wall():
    while not is_wall():
        step()
go_to_wall()
turn_right()


#Kuna ei lubanud paint() kasutada tsüklis siis pidin kordama samad mudelit
go_to_wall()
turn_right()
paint_x()

go_to_wall()
turn_right()
paint_x()


go_to_wall()
turn_right()
paint_x()


go_to_wall()
turn_right()
paint_x()
