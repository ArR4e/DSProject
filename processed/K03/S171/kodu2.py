from pykkar import*
create_world("""
###########
#         #
#         #
#      ^  #
###########""")

 
while not is_wall():
    step()
    
nurgas = False
for x in range(0,3):
    right()
    if is_wall() == True:
        nurgas = True

if nurgas == False:
    while not is_wall():
        step()
        
while not is_painted():
    paint()
    while is_wall():
        right()
    while not is_wall():
        step()
        
done()






