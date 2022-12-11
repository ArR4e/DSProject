import turtle

piip = turtle.Turtle()
piip.color("violet")
piip.pensize(4)
piip.shape('turtle')
piip.speed(0)

# sügavus: mitu erinevat ruudusuurust tehakse
def ruut(sügavus,level):
    
    x = 400/(2**level)
    
    # kui tegemist on viimase (väikseima) ruudu joonistamisega
    # siis tehakse täisruut
    if level == sügavus:
        piip.forward(x)
        piip.right(90)
        piip.forward(x)
        piip.right(90)
        piip.forward(x)
        piip.right(90)
        piip.forward(x)
        
    
    else:
        piip.forward(x)
        piip.left(90)
        ruut(sügavus,level+1)
        piip.left(90)
        piip.forward(x)
        piip.left(90)
        ruut(sügavus,level+1)
        piip.left(90)
        piip.forward(x)
        piip.left(90)
        ruut(sügavus,level+1)
        piip.left(90)
        piip.forward(x)

ruut(7,1)