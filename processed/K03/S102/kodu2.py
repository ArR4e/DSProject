from pykkar import*
a=0
b=0
c=0
create_world("""
#########
#       #
#       #
#   <   #
#########""")
for c in range(6):
    while not is_wall():
        step()
        
    if is_wall()and b!=0:
        paint()
    b+=1  
    while is_wall():
        right()
        a+=1
        if a==2:
            right()
        a=0
exitonclick()
        