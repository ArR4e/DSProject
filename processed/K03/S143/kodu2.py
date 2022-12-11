from pykkar import *

create_world("""
########
#<     #
#      #
#      #
#      #
#      #
########
""")
nesw={"N":0,"E":0,"S":0,"W":0}
def aps():
    for i in range(4):
        nesw[get_direction()] = 1 if is_wall() else 0
        right()
    return [k for k,v in nesw.items() if v==1]
def kt():
    if len(aps()) == 1:
        if aps()[0]=="N":
            if get_direction()=="N":
                right()
            elif get_direction()=="W":
                right()
                right()
            elif get_direction()=="S":
                right()
                right()
                right()
        elif aps()[0]=="W":
            if get_direction()=="W":
                right()
            elif get_direction()=="S":
                right()
                right()
            elif get_direction()=="E":
                right()
                right()
                right()
        elif aps()[0]=="S":
            if get_direction()=="S":
                right()
            elif get_direction()=="E":
                right()
                right()
            elif get_direction()=="N":
                right()
                right()
                right()
        elif aps()[0]=="E":
            if get_direction()=="E":
                right()
            elif get_direction()=="N":
                right()
                right()
            elif get_direction()=="W":
                right()
                right()
                right()
    else:
        paint()
        if ("N" in aps() and "W" in aps()):
            if get_direction()=="N":
                right()
            elif get_direction()=="W":
                right()
                right()
            elif get_direction()=="S":
                right()
                right()
                right()
        elif ("S" in aps() and "W" in aps()):
            if get_direction()=="W":
                right()
            elif get_direction()=="S":
                right()
                right()
            elif get_direction()=="E":
                right()
                right()
                right()
        elif ("S" in aps() and "E" in aps()):
            if get_direction()=="S":
                right()
            elif get_direction()=="E":
                right()
                right()
            elif get_direction()=="N":
                right()
                right()
                right()
        elif ("N" in aps() and "E" in aps()):
            if get_direction()=="E":
                right()
            elif get_direction()=="N":
                right()
                right()
            elif get_direction()=="W":
                right()
                right()
                right()
kt()
i=1
while i <= (5 if len(aps())==1 else 4): 
    while not is_wall():
        step()
    paint()
    right()
    i+=1
        
        
