from turtle import forward, left

def draw_polygon(num_of_sides, side_length):
    angle = 360 / num_of_sides

    for side in range(num_of_sides):
        forward(side_length)
        left(angle)

draw_polygon(30, 50)
