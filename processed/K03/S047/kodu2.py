from pykkar import*

create_world("""
###########
#         #
#         #
#         #
#     >   #
#         #
#         #
###########
""")
i = 1
while not is_wall():
    step()
right()

while i<5 :

    while not is_wall():
        step()
    
    right()
    paint()
    i += 1
