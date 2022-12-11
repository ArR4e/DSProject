from random import randint, choice
from turtle import *

def hulknurk(pikkus,küljed):
    sisenurk = ((küljed-2) * 180)/küljed
    for n in range(küljed):
        fd(pikkus)
        lt(180-sisenurk)
  
colors = ["yellow", "gold", "orange", "red", "maroon",
          "violet", "magenta", "purple", "navy", "blue", "skyblue",
          "cyan", "turquoise", "lightgreen", "green", "darkgreen",
          "chocolate", "brown", "gray"]
speed("fastest")
    
for _ in range(0,30):
    pencolor(choice(colors))
    fillcolor(choice(colors))
    begin_fill()
    hulknurk(randint(20,150),randint(3,13))
    end_fill()
    up()
    goto(randint(-200,200),randint(-300,200))
    down()
    