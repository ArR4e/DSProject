from pykkar import *

world = ""

with open("maailm.txt") as f:
    lines = f.readlines()
    for line in lines:
        world += line
    print(world)
    create_world(world)
    
while not is_wall():
    step()
    
for i in range(4):
    right()
    while not is_wall():
        step()
    paint()
    
    